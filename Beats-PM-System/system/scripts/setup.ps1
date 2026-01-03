# Hydration Script (PowerShell)
# Private by Design: This script copies templates to active files ONLY if they don't exist.
# It ensures your local environment is ready for data without overwriting anything.

$templates = @(
    @{ Template = "Beats-PM-System/TEMPLATES/SETTINGS_TEMPLATE.md"; Target = "SETTINGS.md" },
    @{ Template = "Beats-PM-System/TEMPLATES/bug-report.md"; Target = "5. Trackers/bugs/bugs-master.md" },
    @{ Template = "Beats-PM-System/TEMPLATES/boss-request.md"; Target = "5. Trackers/critical/boss-requests.md" },
    @{ Template = "Beats-PM-System/TEMPLATES/meeting-notes.md"; Target = "5. Trackers/critical/escalations.md" },
    @{ Template = "Beats-PM-System/TEMPLATES/feature-request.md"; Target = "5. Trackers/projects/projects-master.md" }
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
$dirs = @("MEETINGS", "_INBOX/screenshots", "_INBOX/requests", "_INBOX/responses", "DATA", "RESEARCH", "5. Trackers/bugs", "5. Trackers/critical", "5. Trackers/projects")
foreach ($dir in $dirs) {
    if (-not (Test-Path $dir)) {
        New-Item -ItemType Directory -Path $dir | Out-Null
        Write-Host "  [+] Created Directory $dir/" -ForegroundColor Green
    }
}

Write-Host "`n✅ Brain is ready. Your privacy is secured." -ForegroundColor Cyan
Write-Host "Active files are ignored by git. You can now add your real data." -ForegroundColor Yellow
Start-Sleep -Seconds 3
