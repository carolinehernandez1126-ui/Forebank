"""Offline integrity check. Standard library only; no credentials or network."""

import hashlib
import json
import re
from pathlib import Path, PurePosixPath
from zipfile import ZipFile

BASE = Path(__file__).resolve().parent
if not __debug__:
    raise RuntimeError("Run without -O: integrity assertions must stay enabled.")


def sha(data):
    return hashlib.sha256(data).hexdigest()


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"), allow_nan=False).encode()


def verify(base=BASE):
    sums = base / "SHA256SUMS.txt"
    if sums.exists():
        for line in sums.read_text(encoding="utf-8").splitlines():
            expected, name = line.split("  ", 1)
            target = (base / name).resolve()
            assert target.is_relative_to(base.resolve()), "Unsafe checksum path"
            assert sha(target.read_bytes()) == expected, ("Top-level file hash", name)
    manifest = json.loads((base / "MANIFIESTO.json").read_text(encoding="utf-8"))
    index = json.loads((base / "INDICE_RESULTADOS.json").read_text(encoding="utf-8"))
    members = manifest["members"]
    dataset_count = 0
    claude_dataset_count = 0
    source_count = 0
    checked = 0
    for archive in manifest["archives"]:
        p = base / archive["file"]
        assert sha(p.read_bytes()) == archive["sha256"], ("Archive hash mismatch", p.name)
        declared = {v["member"]: v for v in members if v["archive"] == p.name}
        with ZipFile(p) as z:
            assert len(z.namelist()) == len(set(z.namelist())), "Duplicate ZIP members"
            assert set(z.namelist()) == set(declared), ("Archive inventory mismatch", p.name)
            for name, entry in declared.items():
                path = PurePosixPath(name)
                assert not path.is_absolute() and ".." not in path.parts and "\\" not in name
                assert not any(x.lower().startswith(".env") for x in path.parts), (
                    "Environment file included"
                )
                data = z.read(name)
                assert sha(data) == entry["distributed_sha256"] and len(data) == entry["bytes"], (
                    name
                )
                assert not re.search(
                    rb"(?:gh[pousr]_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,}|-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----)",
                    data,
                ), ("Credential signature", name)
                if name.endswith(".json"):
                    value = json.loads(data.decode("utf-8-sig"))
                    if isinstance(value, dict) and "instrument" in value and "candles" in value:
                        assert not value["synthetic"]
                        assert sha(canonical(value)) == entry["dataset_sha256"]
                        if entry.get("producer") == "Claude":
                            claude_dataset_count += 1
                        else:
                            dataset_count += 1
                    if isinstance(value, dict) and "body" in value and "body_sha256" in value:
                        assert sha(canonical(value["body"])) == value["body_sha256"], (
                            "Provider body hash",
                            name,
                        )
                        source_count += 1
                    if isinstance(value, dict):
                        assert not (
                            "day_start_equity" in value
                            or "equity" in value
                            and "positions" in value
                        ), ("Account-like payload", name)
                checked += 1
    assert len(index["primary_rows"]) == 70 and len({v["row"] for v in index["primary_rows"]}) == 70
    assert sum("dataset_member" in v for v in index["primary_rows"]) == 68
    assert dataset_count == 75 and manifest["summary"]["all_normalized_snapshots"] == 75
    by_path = {(v["archive"], v["member"]): v for v in members}
    with ZipFile(base / "02_codex_analisis.zip") as z:
        for row in index["primary_rows"]:
            if "dataset_member" not in row:
                continue
            assert (
                by_path[(row["dataset_archive"], row["dataset_member"])]["dataset_sha256"]
                == row["dataset_sha256"]
            )
            dossier = json.loads(z.read(row["dossier_member"]).decode("utf-8-sig"))
            assert dossier["dataset_sha256"] == row["dataset_sha256"]
    assert index["claude_private_results_included"] is True
    assert (
        manifest["authorized_claude_export"]["real_accounts_orders_fills_journals_included"]
        is False
    )
    assert claude_dataset_count == manifest["summary"]["claude_normalized_snapshots"] == 11
    assert len(index["claude_authorized_research"]["long_histories"]) == 28
    return {
        "status": "PASS",
        "archives": len(manifest["archives"]),
        "members_checked": checked,
        "dataset_snapshots": dataset_count,
        "claude_dataset_snapshots": claude_dataset_count,
        "primary_spot_assets": 68,
        "input_rows": 70,
        "provider_envelopes_checked": source_count,
        "network_used": False,
        "account_data_included": False,
        "claude_authorized_research_included": True,
        "claude_strategy_replay_performed": False,
    }


if __name__ == "__main__":
    print(json.dumps(verify(), ensure_ascii=False, indent=2))
