#!/usr/bin/env python3
"""Nested function call flow extractor for FA PHP source (like cflow)."""
import os, re, sys

root = "/home/kevin/Documents/ksf_Infrastructure/FA/2.4.3"
out = os.path.expanduser("~/Documents/FAAnalysis/FA_CallFlow.txt")

func_def_re = re.compile(r'function\s+(\w+)\s*\(')
# Find calls: word followed by ( - filter out language constructs
call_re = re.compile(r'(?<!function\s)(?<!\$this->)(?<!\w->)(\w+)\s*\(')

funcs = {}
for dirpath, dirs, files in os.walk(root):
    for fname in files:
        if not fname.endswith('.php'):
            continue
        path = os.path.join(dirpath, fname)
        rel = os.path.relpath(path, root)
        try:
            with open(path, 'r', errors='ignore') as f:
                content = f.read()
                lines = content.splitlines()
        except Exception:
            continue
        current_func = None
        indent_level = 0
        for i, line in enumerate(lines, 1):
            # Very rough indent tracking
            stripped = line.lstrip()
            indent_level = len(line) - len(stripped)
            m = func_def_re.search(stripped)
            if m:
                current_func = m.group(1)
                funcs.setdefault(current_func, {"file": rel, "line": i, "calls": set(), "calls_lines": []})
            if current_func:
                # Find calls on this line
                calls = call_re.findall(stripped)
                for c in calls:
                    # Filter out keywords and language constructs
                    ignore = {"if", "while", "for", "switch", "function", "echo", "print", "return", "include", "include_once", "require", "require_once", "else", "elseif", "empty", "isset", "unset", "array", "count", "strtolower", "strtoupper", "strpos", "str_replace", "trim", "explode", "implode", "join", "in_array", "is_array", "is_string", "is_int", "is_numeric", "strlen", "substr", "date", "time", "file_exists", "file_get_contents", "fopen", "fclose", "fwrite", "fread", "die", "exit", "global", "static", "public", "private", "protected", "new", "class", "true", "false", "null", "and", "or", "xor", "instanceof", "as", "use", "namespace", "throw", "catch", "try", "finally", "yield"}
                    if c in ignore or c == current_func:
                        continue
                    funcs[current_func]["calls"].add(c)
                    funcs[current_func]["calls_lines"].append(f"  {'  ' * (indent_level // 4)}{c}()")

with open(out, 'w') as f:
    f.write("# FA Nested Function Call Flow (like cflow)\n\n")
    f.write("Format: Function -> indented direct calls (indent approximates nesting)\n\n")
    for name in sorted(funcs):
        info = funcs[name]
        f.write(f"{name}()  [{info['file']}:{info['line']}]\n")
        # Deduplicate and indent roughly
        unique_calls = sorted(set(info["calls_lines"]))
        # Better: build a simple indented list using indentation from source
        seen = set()
        for line_str in info["calls_lines"]:
            # Extract call name
            call_name = line_str.strip().split()[0]
            if call_name not in seen:
                seen.add(call_name)
                f.write(f"  {line_str.lstrip()}\n")
        f.write("\n")
print(f"Wrote nested call flow to {out} ({len(funcs)} functions)")
