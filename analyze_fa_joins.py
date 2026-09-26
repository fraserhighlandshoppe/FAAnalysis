#!/usr/bin/env python3
"""Phase 2: Analyze SQL joins for missing FK references and decompose joins."""
import os, re, sys

root = "/home/kevin/Documents/ksf_Infrastructure/FA/2.4.3"
out = os.path.expanduser("~/Documents/FA_FK_Join_Report.md")

# Simple parser for schema SQL files to grab table names, columns, PK, KEY
# Then scan .sql files under sql/

schema_tables = {}

sql_files = [os.path.join(root, "sql", f) for f in os.listdir(os.path.join(root, "sql")) if f.endswith('.sql')]

for sql_path in sql_files:
    try:
        content = open(sql_path, 'r', errors='ignore').read()
    except Exception:
        continue
    # Find CREATE TABLE blocks
    # Split by DROP/CREATE pairs roughly
    tables = re.split(r'DROP TABLE IF EXISTS', content)
    for block in tables:
        m = re.search(r'CREATE TABLE IF NOT EXISTS `([^`]+)` \(', block, re.IGNORECASE)
        if not m:
            continue
        tname = m.group(1)
        # Extract column definitions (simple)
        cols = re.findall(r'`([^`]+)`\s+[^,]+', block)
        # Extract PRIMARY KEY
        pk = re.search(r'PRIMARY KEY \(`([^`)]+)`\)', block)
        pk_col = pk.group(1) if pk else None
        # Extract all KEY definitions
        keys = re.findall(r'KEY `([^`]+)` \(([^)]+)\)', block)
        schema_tables[tname] = {
            "cols": cols,
            "pk": pk_col,
            "keys": keys  # list of (key_name, columns_str)
        }

with open(out, 'w') as f:
    f.write("# FA 2.4.3 Phase 2: Join / Foreign Key Analysis\n\n")
    f.write("Schema extracted from `.sql` files.\n\n")
    f.write("| Table | Columns | PK | Keys | Missing FK Notes |\n")
    f.write("|-------|---------|----|------|------------------|\n")
    for tname, info in sorted(schema_tables.items()):
        cols_str = ", ".join(info['cols'][:15]) + ("..." if len(info['cols']) > 15 else "")
        pk_str = info['pk'] or "NONE"
        keys_str = "; ".join([f"{k[0]}({k[1]})" for k in info['keys']])
        # Basic heuristic: if no keys listed besides PK, note it
        note = ""
        if not info['keys']:
            note = "No non-PK indexes; joins may miss keys."
        else:
            # Check if common join columns appear in keys
            pass
        f.write(f"| `{tname}` | {cols_str} | `{pk_str}` | {keys_str} | {note} |\n")
    f.write("\n---\n")
    f.write("**Recommendation:** Tables with no foreign-key constraints should have FK checks added for common join pairs observed in queries (e.g., `debtor_trans.debtor_no` -> `debtors_master.debtor_no`).\n")
    f.write("\nNext: Decompose joins from `FA_Queries.md` and cross-reference with schema above.\n")

print(f"Wrote Phase 2 report to {out} ({len(schema_tables)} tables)")
