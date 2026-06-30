# -*- coding: utf-8 -*-
"""
Logging Service.
Responsible for isolated logging and automatic secret redaction.
"""

class LoggingService:
    def __init__(self):
        self._secrets = set()

    def register_secret(self, secret: str):
        """Register a secret string to be redacted from logs."""
        if secret and len(secret) > 3:
            self._secrets.add(secret)

    def _redact(self, message: str) -> str:
        """Redact known secrets from the message."""
        redacted = message
        for secret in self._secrets:
            redacted = redacted.replace(secret, "********")
        return redacted

    def debug(self, msg: str):
        self._log("DEBUG", msg)

    def info(self, msg: str):
        self._log("INFO", msg)

    def warning(self, msg: str):
        self._log("WARNING", msg)

    def error(self, msg: str):
        self._log("ERROR", msg)

    def _log(self, level: str, msg: str):
        # In a real Kodi addon, this would use xbmc.log
        # But we keep it decoupled so the Kernel can test it easily.
        redacted_msg = self._redact(msg)
        print(f"[SAILE] [{level}] {redacted_msg}")

def logging_factory():
    return LoggingService()
