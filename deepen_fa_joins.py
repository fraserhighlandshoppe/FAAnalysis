#!/usr/bin/env python3
"""Deep Phase 2: Cross-reference JOIN pairs with schema keys."""
import os, re

root = "/home/kevin/Documents/ksf_Infrastructure/FA/2.4.3"
query_md = os.path.expanduser("~/Documents/FA_Queries.md")
report = os.path.expanduser("~/Documents/FA_Phase2_Deep.md")

# Load schema (reuse from previous extraction logic quickly)
schema_path = os.path.expanduser("~/Documents/FA_FK_Join_Report.md")
# We'll build a quick schema dict by parsing sql files directly
schema = {}
for f in os.listdir(os.path.join(root, "sql")):
    if not f.endswith(".sql"): continue
    content = open(os.path.join(root, "sql", f), errors='ignore').read()
    for block in re.split(r'DROP TABLE IF EXISTS', content):
        m = re.search(r'CREATE TABLE IF NOT EXISTS `([^`]+)` \(', block, re.IGNORECASE)
        if m:
            tname = m.group(1)
            cols = set(re.findall(r'`([^`]+)`\s+[^,]+', block))
            pk = re.search(r'PRIMARY KEY \(`([^`)]+)`\)', block)
            pk_col = pk.group(1) if pk else None
            keys = re.findall(r'KEY `([^`]+)` \(([^)]+)\)', block)
            key_cols = set()
            for k in keys:
                for c in k[1].split(','):
                    key_cols.add(c.strip().strip('`'))
            schema[tname] = {"cols": cols, "pk": pk_col, "key_cols": key_cols}

# Extract JOIN references from FA_Queries.md or directly from source
join_refs = []
with open(query_md, 'r', errors='ignore') as f:
    for line in f:
        if 'JOIN' not in line:
            continue
        # Extract SQL table references (strip TB_PREF and quotes) and column pairs
        # Pattern: table AS alias or table alias or table.column
        # Get all table names mentioned near JOIN and all column references in ON clause
        line_text = line.strip()
        # Extract table names after TB_PREF. or quoted
        tables_found = re.findall(r'TB_PREF\."([^"]+)"', line_text)
        # Also find alias references like AS a or alias ON
        aliases = re.findall(r'AS\s+(\w+)', line_text, re.IGNORECASE)
        # Extract ON clause
        on_match = re.search(r'ON\s+(.+)', line_text)
        refs_for_line = []
        if on_match:
            on_clause = on_match.group(1)
            # Find column references in ON: alias.col or table.col
            col_refs = re.findall(r'(?:\w+)\.([\w_]+)', on_clause)
            # Pair them loosely; just record clause for manual inspection
            refs_for_line.append(f"ON {on_clause}")
        # Build reference entry
        entry_refs = {"line": line_text[:200], "tables": tables_found + aliases, "on_clause": refs_for_line}
        join_refs.append(entry_refs)

with open(report, 'w') as out:
    out.write("# Phase 2 Deep: Missing FK / Key Analysis\n\n")
    out.write("Schema parsed from `.sql`; joins parsed from `FA_Queries.md`.\n\n")
    out.write("| Source Line | JOIN Reference | Referenced Table Key Status | Note |\n")
    out.write("|-------------|----------------|----------------------------|------|\n")
    for item in join_refs[:100]:
        line_snippet = item['line']
        tables = item['tables']
        on_clause = item['on_clause']
        note = ""
        # Check each table found in the JOIN line against schema keys for columns used in ON
        # For simplicity, extract column references from ON clause and check against referenced tables
        for on_text in on_clause:
            # Find column references in the ON text
            cols_found = re.findall(r'\w+\.([\w_]+)', on_text)
            for col in cols_found:
                # Try to associate column with any table in line (approximate)
                for tname in tables:
                    info = schema.get(tname)
                    if info:
                        if info['pk'] == col or col in info['key_cols']:
                            status = "PK/Indexed"
                        else:
                            status = "NOT key/index"
                            note += f"Table `{tname}` column `{col}` is NOT indexed; "
                    else:
                        # Try stripping common prefixes (e.g., '0_')
                        base_t = tname.lstrip('0_') if tname.startswith('0_') else tname
                        info2 = schema.get(base_t)
                        if info2:
                            if info2['pk'] == col or col in info2['key_cols']:
                                status = "PK/Indexed"
                            else:
                                status = "NOT key/index"
                                note += f"Table `{base_t}` column `{col}` is NOT indexed; "
                        else:
                            note += f"Table `{tname}` not found in schema; "
        refs_str = f"Tables: {', '.join(tables)}; ON: {' | '.join(on_clause)}"
        if note:
            out.write(f"| `{line_snippet}` | `{refs_str}` | `{note}` | This should be a FK or index needs adding |\n")
        else:
            out.write(f"| `{line_snippet}` | `{refs_str}` | All referenced keys present | OK |\n")
    out.write(f"\n**Total JOIN references scanned:** {len(join_refs)}\n")
    out.write("**Recommendation:** For any `NOT key/index` reference, verify whether the column is an intended foreign key. If yes, add `FOREIGN KEY` constraint or at minimum an index to prevent missing records due to missing category references.\n")

print(f"Wrote deep Phase 2 report to {report} ({len(join_refs)} references checked)")
