from __future__ import annotations

import json
import sqlite3
from pathlib import Path

from .io import canonical, digest, utcnow


class Store:
    """Content-addressed source snapshots + append-only audit journal, local only."""

    def __init__(self, path="data/lab.sqlite"):
        Path(path).parent.mkdir(parents=True, exist_ok=True)
        self.db = sqlite3.connect(path)
        self.db.execute("PRAGMA journal_mode=WAL")
        self.db.executescript("""
            CREATE TABLE IF NOT EXISTS sources (
                id TEXT PRIMARY KEY, request_key TEXT NOT NULL,
                fetched_at TEXT NOT NULL, body TEXT NOT NULL
            );
            CREATE INDEX IF NOT EXISTS source_request ON sources(request_key, fetched_at);
            CREATE TABLE IF NOT EXISTS journal (
                id INTEGER PRIMARY KEY AUTOINCREMENT, at TEXT NOT NULL,
                kind TEXT NOT NULL, payload TEXT NOT NULL, sha256 TEXT NOT NULL
            );
        """)

    def close(self):
        self.db.close()

    def cached(self, request_key, ttl):
        from datetime import datetime

        row = self.db.execute(
            "SELECT body, fetched_at FROM sources WHERE request_key=? ORDER BY fetched_at DESC LIMIT 1",
            (request_key,),
        ).fetchone()
        if row and 0 <= (utcnow() - datetime.fromisoformat(row[1])).total_seconds() < ttl:
            return json.loads(row[0])
        return None

    def save_source(self, request_key, envelope):
        self.db.execute(
            "INSERT OR IGNORE INTO sources VALUES (?, ?, ?, ?)",
            (digest(envelope), request_key, envelope["fetched_at"], canonical(envelope)),
        )
        self.db.commit()

    def audit(self, kind, payload):
        self.db.execute(
            "INSERT INTO journal(at, kind, payload, sha256) VALUES (?, ?, ?, ?)",
            (utcnow().isoformat(), kind, canonical(payload), digest(payload)),
        )
        self.db.commit()

    def events(self):
        rows = self.db.execute("SELECT id, at, kind, payload, sha256 FROM journal ORDER BY id")
        return [
            dict(id=r[0], at=r[1], kind=r[2], payload=json.loads(r[3]), sha256=r[4]) for r in rows
        ]
