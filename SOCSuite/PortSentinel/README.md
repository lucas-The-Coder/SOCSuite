# PortSentinel - Port Scanner for SOC Network Recon

Junior SOC Analyst project. Scans a host for open ports to find exposed services.

## What it does

Tries to connect to common ports on a host. If connect works, port is OPEN, else CLOSED.

Think like SOC: Attacker scans for open ports, defender checks what is exposed.

## Files

- scanner.py - Scanner code
- README.md - This file

## How to run

python3 scanner.py
python3 scanner.py 127.0.0.1

## Tests

- python3 scanner.py
- Expected on Nobara with Postgres running:
  21 CLOSED
  22 CLOSED
  80 CLOSED
  443 CLOSED
  3306 CLOSED
  5432 OPEN
  8000 CLOSED
  [5432]

5432 OPEN means Postgres is exposed, others closed is good.

## How it works

- scan_port(host, port) - Create socket, set timeout 1 sec, try connect_ex, return True if 0 else False, close socket
- scan_host(host) - Loop ports list [21, 22, 80, 443, 3306, 5432, 8000], call scan_port for each, collect open ports in list
- main() - Get host from terminal with sys.argv, default 127.0.0.1, call scan_host, print open ports

## Skills

Python, Sockets, Network recon, sys.argv, SOC triage
