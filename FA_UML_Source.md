# FA 2.4.3 UML / Flow Chart Sources

## PHPDocumentor Source Installation
- Installed via Composer at `~/Documents/phpdoc/`
- Source: `~/Documents/phpdoc/vendor/phpdocumentor/phpdocumentor`
- Binary: `~/Documents/phpdoc/vendor/bin/phpdoc`
- Template output: `~/Documents/phpdoc_output/`

Usage (example):
```bash
~/Documents/phpdoc/vendor/bin/phpdoc -d /home/kevin/Documents/ksf_Infrastructure/FA/2.4.3 -t ~/Documents/phpdoc_output --title="FA 2.4.3" --name="ksfraser/fa" --force
```

Note: PHPDocumentor produces **class diagrams** (UML) and documentation, not logic-flow (if/else) charts. The logic-flow charts below are manually produced from source inspection.

---

## Logic Flow Chart (PlantUML) - Entry Point Example: `frontaccounting.php`

Source file logic extracted manually:
- Includes session/auth checks
- Includes company selection
- Includes module routing
- If mode set, include module file; else include dashboard/page

PlantUML source saved at: `~/Documents/FA_UML_Flow.puml`
