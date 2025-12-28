# Hydration Script (PowerShell)
# Private by Design: This script copies templates to active files ONLY if they don't exist.
# It ensures your local environment is ready for data without overwriting anything.

$templates = @(
    @{ Template = "SETTINGS_TEMPLATE.md"; Target = "SETTINGS.md" },
    @{ Template = "BUGS/bugs-master_TEMPLATE.md"; Target = "BUGS/bugs-master.md" },
    @{ Template = "CRITICAL/boss-requests_TEMPLATE.md"; Target = "CRITICAL/boss-requests.md" },
    @{ Template = "CRITICAL/escalations_TEMPLATE.md"; Target = "CRITICAL/escalations.md" },
    @{ Template = "PROJECTS/projects-master_TEMPLATE.md"; Target = "PROJECTS/projects-master.md" },
    @{ Template = "PEOPLE/engineering-items_TEMPLATE.md"; Target = "PEOPLE/engineering-items.md" },
    @{ Template = "PEOPLE/stakeholders_TEMPLATE.md"; Target = "PEOPLE/stakeholders.md" },
    @{ Template = "PEOPLE/ux-tasks_TEMPLATE.md"; Target = "PEOPLE/ux-tasks.md" }
)

Write-Host "🧠 Hydrating Antigravity Brain..." -ForegroundColor Cyan

foreach ($item in $templates) {
    if (-not (Test-Path $item.Target)) {
        Copy-Item $item.Template $item.Target
        Write-Host "  [+] Created $($item.Target)" -ForegroundColor Green
    } else {
        Write-Host "  [skip] $($item.Target) (Exists)" -ForegroundColor DarkGray
    }
}

# Ensure Directories Exist
$dirs = @("MEETINGS", "_INBOX/screenshots", "DATA", "RESEARCH")
foreach ($dir in $dirs) {
    if (-not (Test-Path $dir)) {
        New-Item -ItemType Directory -Path $dir | Out-Null
        Write-Host "  [+] Created Directory $dir/" -ForegroundColor Green
    }
}

Write-Host "`n✅ Brain is ready. Your privacy is secured." -ForegroundColor Cyan
Write-Host "Active files are ignored by git. You can now add your real data." -ForegroundColor Yellow
Start-Sleep -Seconds 3
