"""Send insider-buy alerts to Discord, Slack and/or Telegram.

Channels are enabled by environment variables:
  STOCKTRACK_DISCORD_WEBHOOK      Discord channel webhook URL
  STOCKTRACK_SLACK_WEBHOOK        Slack incoming-webhook URL
  STOCKTRACK_TELEGRAM_BOT_TOKEN   Telegram bot token (from @BotFather) ...
  STOCKTRACK_TELEGRAM_CHAT_ID     ... and the chat to post in
"""

from __future__ import annotations

import json
import logging
import os
import urllib.request
from dataclasses import dataclass

from stocktrack.signals import money, qty
from stocktrack.tracker import Signal

log = logging.getLogger(__name__)

ICONS = {"Strong": "\U0001f525", "Notable": "⭐", "Minor": "•"}


def format_alert(sig: Signal) -> str:
    b, s = sig.buy, sig.score
    who = b.owner_name + (f" ({b.officer_title or b.role})" if b.role != "Other" else "")
    when = b.last_date if b.first_date == b.last_date else f"{b.first_date} to {b.last_date}"
    price = f" @ ${b.avg_price:,.2f}" if b.avg_price else ""
    value = f" = {money(b.value)}" if b.value else ""
    lines = [
        f"{ICONS[s.label]} {s.label} insider buy: {b.ticker or b.issuer_name} (score {s.total}/100)",
        b.issuer_name,
        f"{who} bought {qty(b.shares)} sh{price}{value} on {when}",
    ]
    if s.tags:
        lines.append(" | ".join(s.tags))
    if sig.quote and b.avg_price:
        chg = sig.quote.change_from(b.avg_price)
        lines.append(f"Now ${sig.quote.price:,.2f} ({chg:+.1%} vs insider price)")
    lines.append(b.url)
    return "\n".join(lines)


@dataclass
class Channel:
    name: str
    url: str
    payload_key: str
    extra: dict

    def send(self, text: str, timeout: float = 15.0) -> None:
        body = json.dumps({self.payload_key: text, **self.extra}).encode()
        req = urllib.request.Request(self.url, data=body, headers={"Content-Type": "application/json"})
        with urllib.request.urlopen(req, timeout=timeout):
            pass


class Notifier:
    def __init__(self, channels: list[Channel]) -> None:
        self.channels = channels

    @classmethod
    def from_env(cls, env: dict[str, str] | None = None) -> "Notifier":
        env = dict(os.environ) if env is None else env
        channels = []
        if env.get("STOCKTRACK_DISCORD_WEBHOOK"):
            channels.append(Channel("discord", env["STOCKTRACK_DISCORD_WEBHOOK"], "content", {}))
        if env.get("STOCKTRACK_SLACK_WEBHOOK"):
            channels.append(Channel("slack", env["STOCKTRACK_SLACK_WEBHOOK"], "text", {}))
        token, chat = env.get("STOCKTRACK_TELEGRAM_BOT_TOKEN"), env.get("STOCKTRACK_TELEGRAM_CHAT_ID")
        if token and chat:
            channels.append(
                Channel(
                    "telegram",
                    f"https://api.telegram.org/bot{token}/sendMessage",
                    "text",
                    {"chat_id": chat, "disable_web_page_preview": True},
                )
            )
        return cls(channels)

    @property
    def names(self) -> list[str]:
        return [c.name for c in self.channels]

    def send(self, text: str) -> dict[str, str | None]:
        """Send to every channel; returns channel -> error message (None on success)."""
        results: dict[str, str | None] = {}
        for c in self.channels:
            try:
                c.send(text[:1900] if c.name == "discord" else text)
                results[c.name] = None
            except Exception as e:  # one broken channel shouldn't stop the others
                log.warning("alert via %s failed: %s", c.name, e)
                results[c.name] = str(e)
        return results
