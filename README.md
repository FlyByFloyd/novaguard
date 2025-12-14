# NovaGuard v1

NovaGuard is a small, local security scanning tool written in Python.

It is designed to give quick confidence that nothing obvious is wrong on a single machine, without dashboards, cloud services, or background processes.

NovaGuard runs entirely locally from the terminal.

---

## What NovaGuard v1 Does

NovaGuard v1 performs two simple checks:

### 1. Local Port Scan
- Scans localhost for a small set of common, high-risk ports
- Helps identify accidentally exposed services
- Uses safe timeouts and does not perform aggressive scanning

### 2. Risky File Scan
- Recursively scans a chosen folder
- Detects potentially risky file types (e.g. `.exe`, `.bat`, `.ps1`)
- Skips virtual environments and cache folders to avoid false positives
- Reports a short, readable summary

---

## What NovaGuard v1 Does NOT Do

- No GUI
- No web interface
- No cloud connectivity
- No accounts or authentication
- No background services
- No automatic remediation

This project is intentionally small, focused, and easy to understand.

---

## Requirements

- Python 3.x
- Windows (tested on Windows with PowerShell)
- No third-party dependencies

---

## How to Run

Clone the repository and navigate into the project folder:

```bash
git clone https://github.com/FlyByFloyd/novaguard.git
cd novaguard
