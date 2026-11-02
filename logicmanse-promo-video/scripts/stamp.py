#!/usr/bin/env python3
"""Copy deliverables to timestamped names: <name>_YYYY-MM-DD_HHMM<ext> (local time).

Usage: stamp.py FILE [FILE ...] [--dest DIR]
Originals are left untouched (Drive/Metricool links may point at them). Re-running in the same
minute is idempotent. Prints the stamped path of each file.
"""
import shutil, sys, time
from pathlib import Path

args = sys.argv[1:]
dest = None
if "--dest" in args:
    i = args.index("--dest"); dest = Path(args[i + 1]); del args[i:i + 2]
stamp = time.strftime("%Y-%m-%d_%H%M")
for a in args:
    p = Path(a)
    out = (dest or p.parent) / f"{p.stem}_{stamp}{p.suffix}"
    out.parent.mkdir(parents=True, exist_ok=True)
    if not out.exists():
        shutil.copy2(p, out)
    print(out)
