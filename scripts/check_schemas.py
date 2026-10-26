"""Ensure versioned contracts match actual models; no network, no secrets."""

import json
from pathlib import Path

from research_lab.models import Account, Dataset, Proposal, Review, RiskPolicy

for model in (Dataset, Account, Proposal, Review, RiskPolicy):
    path = Path("schemas") / (model.__name__.lower() + ".schema.json")
    assert json.loads(path.read_text(encoding="utf-8")) == model.model_json_schema(), str(path)
print("Contracts match Python models")
