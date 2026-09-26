#!/bin/bash
# Generate PlantUML + PNG for each FA module entry point
ROOT=/home/kevin/Documents/ksf_Infrastructure/FA/2.4.3
OUTDIR=/home/fhs_kevin/Documents
JAVA_CMD="java -jar ~/Documents/plantuml/plantuml.jar -tpng"

for dir in inventory sales purchasing gl reporting admin dimensions fixed_assets taxes access company modules; do
    entry="$ROOT/$dir/index.php"
    if [ -f "$entry" ]; then
        echo "Processing $dir ..."
        # Extract a brief logic description (first 20 non-empty non-comment lines)
        head -n 30 "$entry" | grep -v '^\s*//' | grep -v '^\s*/\*' | grep -v '^\s*\*' > /tmp/${dir}_snippet.txt
        puml="$OUTDIR/FA_UML_${dir}.puml"
        cat > "$puml" << PUML
@startuml
start
:Entry $dir/index.php;
if (access allowed?) then (yes)
  :Load module;
else (no)
  :Redirect / deny;
  stop
endif
:Include functions;
:Process request;
stop
PUML
        $JAVA_CMD "$puml" > /dev/null 2>&1 && echo "  -> PNG: $OUTDIR/FA_UML_${dir}.png"
    fi
done
echo "Done."
