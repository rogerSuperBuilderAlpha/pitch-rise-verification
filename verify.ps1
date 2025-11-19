# Pitch Rise Verification Script
# Verifies the provided verification code.

param(
    [Parameter(Mandatory=$false)]
    [string]$Code
)

# Expected format: PITCH-XXXX-XXXX-XXXX
$pattern = '^PITCH-[A-Z0-9]{4}-[A-Z0-9]{4}-[A-Z0-9]{4}$'

if (-not $Code) {
    $Code = Read-Host "Enter verification code"
}

if ($Code -match $pattern) {
    Write-Host "Verification code '$Code' is valid!" -ForegroundColor Green
    exit 0
} else {
    Write-Host "Error: Invalid code format. Expected format: PITCH-XXXX-XXXX-XXXX" -ForegroundColor Red
    Write-Host "Provided code: $Code" -ForegroundColor Yellow
    exit 1
}

