from __future__ import annotations

import hashlib
import json
import tomllib
from datetime import UTC, datetime
from pathlib import Path

from pydantic import BaseModel

from .models import RiskPolicy


def utcnow():
    return datetime.now(UTC)


def plain(value):
    if isinstance(value, BaseModel):
        return value.model_dump(mode="json")
    if isinstance(value, datetime):
        return value.isoformat()
    raise TypeError(type(value).__name__)


def canonical(value):
    if isinstance(value, BaseModel):
        value = plain(value)
    return json.dumps(value, sort_keys=True, separators=(",", ":"), default=plain, allow_nan=False)


def digest(value):
    return hashlib.sha256(canonical(value).encode()).hexdigest()


def read_json(path):
    return json.loads(Path(path).read_text(encoding="utf-8-sig"))


def write_json(path, value):
    dest = Path(path)
    dest.parent.mkdir(parents=True, exist_ok=True)
    # Replacement is atomic within the filesystem; readers cannot see partial JSON.
    temp = dest.with_suffix(dest.suffix + ".tmp")
    temp.write_text(
        json.dumps(value, default=plain, indent=2, allow_nan=False) + "\n", encoding="utf-8"
    )
    temp.replace(dest)


def settings(path="config/lab.toml"):
    return tomllib.loads(Path(path).read_text(encoding="utf-8"))


def policy(path="config/lab.toml"):
    return RiskPolicy.model_validate(settings(path)["risk"])


def assets(path="config/assets.toml"):
    return tomllib.loads(Path(path).read_text(encoding="utf-8"))["assets"]
