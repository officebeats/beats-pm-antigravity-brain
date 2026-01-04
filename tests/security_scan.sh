#!/bin/bash

# 🛡️ Antigravity Security Scan
# Prevents sensitive internal names from leaking into the repo.

FORBIDDEN_TERMS=(
    "Route Exchange"
    "Skypro"
    "Gabriel.Duran"
    "Ascension"
    "@ascension.org"
    "@getroute.com"
)

EXIT_CODE=0

echo "🔍 Scanning for sensitive terms..."

for TERM in "${FORBIDDEN_TERMS[@]}"; do
    # Grep recursively, excluding the .git folder and this script itself
    MATCHES=$(grep -r "$TERM" . --exclude-dir=.git --exclude="security_scan.sh" --exclude="SETTINGS.md" --exclude-dir=".gemini")
    
    if [ ! -z "$MATCHES" ]; then
        echo "❌ SECURITY FAILURE: Found forbidden term '$TERM' in:"
        echo "$MATCHES"
        EXIT_CODE=1
    fi
done

if [ $EXIT_CODE -eq 0 ]; then
    echo "✅ Security Scan Passed."
else
    echo "⛔ Commit Blocked. Please sanitize the files above."
fi

exit $EXIT_CODE
