# SOCSuite - Unified SOC Tool

Junior SOC Analyst final project. Connects 4 tools into one scan.

## What it does

Runs BruteGuard + PortSentinel + FileSentinel + IOCSentinel, prints one SOC report.

Think like SOC: One analyst, one report, all evidence together.

## Structure

- soc_suite.py - Suite, runs all 4 tools with subprocess
- BruteGuard/ - Log parser, brute-force detector
- PortSentinel/ - Port scanner, open ports
- FileSentinel/ - File integrity, SHA256 baseline
- IOCSentinel/ - IOC checker, AbuseIPDB API
- README.md - This file

## How to run

pip install -r IOCSentinel/requirements.txt
# Or: pip install requests python-dotenv
python3 soc_suite.py

IOCSentinel needs .env file:
IOCSentinel/.env
ABUSEIPDB_API_KEY=your key here

## Tests

python3 soc_suite.py
Expected:
SOC Suite - Starting Full Scan
=== BruteGuard ===
ALERT {'192.168.1.50': 6, ...}
=== PortSentinel ===
5432 OPEN
=== FileSentinel ===
OK
=== IOCSentinel ===
8.8.8.8 0 CLEAN
1.2.3.4 76 MALICIOUS
SOC Suite - Scan Complete

## How it works

- run_tool(name, command) - subprocess.run(command, capture_output=True, text=True), save result.stdout into output, print === name === + output, return output
- main() - Print Starting, call run_tool for each of 4 tools, print Complete
- Each tool uses os.path.dirname(__file__) to find its own files, so it works from any folder
- IOCSentinel uses .env + load_dotenv, no hardcoded API key

## Skills

Python, Subprocess, Sockets, Hashing SHA256, REST API, Env vars, SOC triage
