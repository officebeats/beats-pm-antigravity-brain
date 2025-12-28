#!/bin/bash
# Mac/Linux Hydration Script

echo "🧠 Hydrating Antigravity Brain..."

# Array of Template -> Target
declare -a files=(
    "SETTINGS_TEMPLATE.md:SETTINGS.md"
    "BUGS/bugs-master_TEMPLATE.md:BUGS/bugs-master.md"
    "CRITICAL/boss-requests_TEMPLATE.md:CRITICAL/boss-requests.md"
    "CRITICAL/escalations_TEMPLATE.md:CRITICAL/escalations.md"
    "PROJECTS/projects-master_TEMPLATE.md:PROJECTS/projects-master.md"
    "PEOPLE/engineering-items_TEMPLATE.md:PEOPLE/engineering-items.md"
    "PEOPLE/stakeholders_TEMPLATE.md:PEOPLE/stakeholders.md"
    "PEOPLE/ux-tasks_TEMPLATE.md:PEOPLE/ux-tasks.md"
)

# Loop and copy
for entry in "${files[@]}"; do
    template="${entry%%:*}"
    target="${entry##*:}"

    if [ ! -f "$target" ]; then
        cp "$template" "$target"
        echo "  [+] Created $target"
    else
        echo "  [skip] $target (Exists)"
    fi
done

# Directories
mkdir -p MEETINGS _INBOX/screenshots DATA RESEARCH

echo ""
echo "✅ Brain is ready."
