"""Polite HTTP client for SEC EDGAR.

The SEC asks automated tools to identify themselves with a User-Agent that
includes a contact email, and to stay under 10 requests per second:
https://www.sec.gov/os/accessing-edgar-data
"""

from __future__ import annotations

import gzip
import logging
import threading
import time
import urllib.error
import urllib.request

log = logging.getLogger(__name__)

SEC_MAX_RPS = 10


class MissingUserAgent(RuntimeError):
    pass


class HttpClient:
    def __init__(
        self,
        user_agent: str,
        max_rps: float = 8.0,
        timeout: float = 30.0,
        retries: int = 4,
    ) -> None:
        if not user_agent or "@" not in user_agent:
            raise MissingUserAgent(
                "SEC EDGAR requires a User-Agent with a contact email, e.g. "
                "'Jane Doe jane@example.com'. Set STOCKTRACK_USER_AGENT or pass --user-agent."
            )
        self.user_agent = user_agent
        self.min_interval = 1.0 / min(max_rps, SEC_MAX_RPS)
        self.timeout = timeout
        self.retries = retries
        self._lock = threading.Lock()
        self._last = 0.0

    def _throttle(self) -> None:
        with self._lock:
            wait = self._last + self.min_interval - time.monotonic()
            if wait > 0:
                time.sleep(wait)
            self._last = time.monotonic()

    def get(self, url: str) -> bytes:
        """GET a URL, retrying on rate limiting, server errors and network failures.

        A 404 is raised immediately as urllib.error.HTTPError.
        """
        delay = 2.0
        for attempt in range(self.retries + 1):
            self._throttle()
            req = urllib.request.Request(
                url,
                headers={"User-Agent": self.user_agent, "Accept-Encoding": "gzip"},
            )
            try:
                with urllib.request.urlopen(req, timeout=self.timeout) as resp:
                    body = resp.read()
                    if resp.headers.get("Content-Encoding") == "gzip":
                        body = gzip.decompress(body)
                    return body
            except urllib.error.HTTPError as e:
                if e.code not in (429, 500, 502, 503, 504) or attempt == self.retries:
                    raise
                log.warning("HTTP %s for %s, retrying in %.0fs", e.code, url, delay)
            except (urllib.error.URLError, TimeoutError, ConnectionError) as e:
                if attempt == self.retries:
                    raise
                log.warning("%s for %s, retrying in %.0fs", e, url, delay)
            time.sleep(delay)
            delay *= 2
        raise AssertionError("unreachable")

    def get_text(self, url: str) -> str:
        return self.get(url).decode("utf-8", errors="replace")
