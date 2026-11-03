#!/usr/bin/env python3
"""LogicManse social post inventory (single source of truth for duplicate checks).

Data file: C:\\Users\\aniph\\OneDrive\\claude\\LogicManse Social Inventory\\social-inventory.json
One row per (asset_key, network). Commands:
  inventory.py check ASSET_KEY NETWORK   exit 1 + prints the row if already posted/scheduled (use BEFORE scheduling)
  inventory.py upsert '<json row>'       insert/replace the row for (asset_key, network)
  inventory.py render                    rewrite social-inventory.md and social-inventory.csv from the JSON
  inventory.py gaps                      list every (asset_key, network) of the 5 networks that has no live row
Row fields: asset_key, book, title, kind, network, status (PUBLISHED|SCHEDULED|PLANNED|FAILED|LEGACY),
  when (America/New_York, YYYY-MM-DD HH:MM), metricool_id, url, source (metricool|legacy), drive_file,
  board, ai_flag (true/false/n-a), notes
"""
import csv, json, sys
from pathlib import Path

DIR = Path(r"C:\Users\aniph\OneDrive\claude\LogicManse Social Inventory")
DATA = DIR / "social-inventory.json"
NETWORKS = ["facebook", "instagram", "tiktok", "youtube", "pinterest"]
COLS = ["asset_key", "book", "title", "kind", "network", "status", "when", "url", "source", "board", "ai_flag", "metricool_id", "drive_file", "notes"]
LIVE = {"PUBLISHED", "SCHEDULED", "PLANNED"}


def load():
    return json.loads(DATA.read_text(encoding="utf-8")) if DATA.exists() else {"rows": []}


def save(d):
    DIR.mkdir(parents=True, exist_ok=True)
    DATA.write_text(json.dumps(d, indent=1, ensure_ascii=False), encoding="utf-8")


def find(d, key, net):
    return next((r for r in d["rows"] if r["asset_key"] == key and r["network"] == net), None)


def render(d):
    rows = sorted(d["rows"], key=lambda r: (r.get("when", ""), r["asset_key"], r["network"]))
    with open(DIR / "social-inventory.csv", "w", newline="", encoding="utf-8-sig") as f:
        w = csv.DictWriter(f, COLS, extrasaction="ignore"); w.writeheader(); w.writerows(rows)
    lines = ["# LogicManse social post inventory", "", "Generated from social-inventory.json. Do not edit by hand; use inventory.py.", "",
             "| Asset | Network | Status | When (ET) | Board | AI flag | Link |", "|---|---|---|---|---|---|---|"]
    for r in rows:
        link = r.get("url") or ""
        lines.append(f"| {r['asset_key']} | {r['network']} | {r['status']} | {r.get('when','')} | {r.get('board','')} | {r.get('ai_flag','')} | {link} |")
    (DIR / "social-inventory.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main():
    a = sys.argv[1:]
    d = load()
    if not a:
        print(__doc__); return
    if a[0] == "check":
        r = find(d, a[1], a[2])
        if r and r["status"] in LIVE | {"LEGACY"}:
            print(json.dumps(r, ensure_ascii=False)); sys.exit(1)
        print("clear"); return
    if a[0] == "upsert":
        row = json.loads(a[1]); old = find(d, row["asset_key"], row["network"])
        if old: old.update(row)
        else: d["rows"].append(row)
        save(d); render(d); print("ok"); return
    if a[0] == "render":
        render(d); print("ok"); return
    if a[0] == "gaps":
        assets = {}
        for r in d["rows"]:
            if r.get("source") == "metricool" or r["status"] in LIVE:
                assets.setdefault(r["asset_key"], {})[r["network"]] = r["status"]
                assets[r["asset_key"]]["_kind"] = r.get("kind", "")
        for k, nets in sorted(assets.items()):
            if k.startswith(("legacy-", "backfill-")): continue  # pre-Metricool or Pinterest-only backfills
            need = ["facebook", "instagram", "pinterest"] if nets.get("_kind") == "image" else NETWORKS  # image posts skip TikTok/YouTube
            miss = [n for n in need if nets.get(n) not in LIVE]
            if miss: print(f"{k}: missing {', '.join(miss)}")
        return


main()
