#!/usr/bin/env python3
import os, re

root = "/home/kevin/Documents/ksf_Infrastructure/FA/2.4.3"
output = os.path.expanduser("~/Documents/FA_Queries.md")

entries = []
# Better pattern: line contains SQL keyword and either db_query, $sql=, or table reference
sql_keyword_re = re.compile(r'\b(SELECT|INSERT|UPDATE|DELETE|CREATE|ALTER|DROP|FROM|JOIN)\b', re.IGNORECASE)
# Lines with DB function calls or SQL variable assignments or SQL file contents
relevant_re = re.compile(r'db_query|db_fetch|mysql_query|mysqli_query|\.TB_PREF\.|TB_PREF|\$sql|\$query', re.IGNORECASE)

for dirpath, dirnames, filenames in os.walk(root):
    for fname in filenames:
        if not (fname.endswith('.php') or fname.endswith('.sql')):
            continue
        path = os.path.join(dirpath, fname)
        try:
            with open(path, 'r', encoding='utf-8', errors='ignore') as f:
                lines = f.read().splitlines()
        except Exception:
            continue
        for i, line in enumerate(lines, 1):
                has_sql_keyword = sql_keyword_re.search(line)
                has_db_ref = relevant_re.search(line)
                # Include .sql files with SQL keywords; for .php require DB reference
                if fname.endswith('.sql'):
                    if has_sql_keyword:
                        entries.append((path, i, line.strip()))
                else:
                    if has_db_ref and has_sql_keyword:
                        entries.append((path, i, line.strip()))

# Deduplicate
seen = set()
unique_entries = []
for e in entries:
    key = (e[0], e[1], e[2])
    if key not in seen:
        seen.add(key)
        unique_entries.append(e)

with open(output, 'w') as out:
    out.write("# FA 2.4.3 SQL Query Inventory\n\n")
    out.write("Source root: `{}`\n\n".format(root))
    out.write("| File | Line | SQL Snippet / Context |\n")
    out.write("|------|------|-----------------------|\n")
    for path, line_no, snippet in unique_entries:
        rel = os.path.relpath(path, root)
        short = snippet[:350].replace('|', '\\|').replace('\n', ' ')
        out.write(f"| `{rel}` | {line_no} | `{short}` |\n")
    out.write(f"\n**Total SQL-related lines captured:** {len(unique_entries)}\n")

print(f"Wrote {len(unique_entries)} entries to {output}")
