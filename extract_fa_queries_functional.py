#!/usr/bin/env python3
import os, re

root = "/home/kevin/Documents/ksf_Infrastructure/FA/2.4.3"
output = os.path.expanduser("~/Documents/FAAnalysis/FA_Queries_Functional.md")

# Directories to include (functional modules/forms)
include_dirs = [
    "access", "admin", "applications", "company", "dimensions",
    "fixed_assets", "gl", "inventory", "manufacturing", "modules",
    "purchasing", "sales", "taxes", "includes/db"
]
exclude_dirs = ["sql", "reporting", "doc", "js", "themes", "tmp", "install"]

func_dirs = []
for d in include_dirs:
    func_dirs.append(os.path.join(root, d))

sql_keyword_re = re.compile(r'\b(SELECT|INSERT|UPDATE|DELETE|CREATE|ALTER|DROP)\b', re.IGNORECASE)
relevant_re = re.compile(r'db_query|mysql_query|mysqli_query|\.TB_PREF\.|TB_PREF|\$sql|\$query', re.IGNORECASE)

entries = []
for base_dir in func_dirs:
    if not os.path.isdir(base_dir):
        continue
    for dirpath, dirs, filenames in os.walk(base_dir):
        # Skip excluded subdirs
        dirs[:] = [d for d in dirs if d not in exclude_dirs]
        for fname in filenames:
            if not (fname.endswith('.php') or fname.endswith('.inc')):
                continue
            path = os.path.join(dirpath, fname)
            rel = os.path.relpath(path, root)
            try:
                with open(path, 'r', encoding='utf-8', errors='ignore') as f:
                    lines = f.read().splitlines()
            except Exception:
                continue
            for i, line in enumerate(lines, 1):
                has_sql = bool(sql_keyword_re.search(line))
                has_db_ref = bool(relevant_re.search(line))
                if has_sql and has_db_ref:
                    snippet = line.strip()[:350].replace('|', '\\|')
                    entries.append((rel, i, snippet))

seen = set()
unique_entries = []
for e in entries:
    key = (e[0], e[1], e[2])
    if key not in seen:
        seen.add(key)
        unique_entries.append(e)

with open(output, 'w') as out:
    out.write("# FA 2.4.3 Functional Query Inventory (CRUD / Forms / Displays)\n\n")
    out.write("Excludes: SQL install/update scripts, reporting queries, docs.\n")
    out.write("Includes: access, admin, applications, company, dimensions, fixed_assets, gl, inventory, manufacturing, modules, purchasing, sales, taxes, includes/db.\n\n")
    out.write("| File | Line | SQL Snippet / Context |\n")
    out.write("|------|------|-----------------------|\n")
    for rel, line_no, snippet in unique_entries:
        out.write(f"| `{rel}` | {line_no} | `{snippet}` |\n")
    out.write(f"\n**Total functional SQL-related lines:** {len(unique_entries)}\n")

print(f"Wrote functional query inventory to {output} ({len(unique_entries)} entries)")
