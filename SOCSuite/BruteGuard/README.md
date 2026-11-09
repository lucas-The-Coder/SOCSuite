# BruteGuard - SSH Brute-Force Detector

Junior SOC Analyst project. Detects brute-force attacks by parsing auth logs.

## What it does

Collects SSH logs, parses failed logins, counts fails per IP, alerts if IP exceeds threshold.

Think like SOC: Collect -> Parse -> Detect -> Alert -> Respond

## Files

- main.py - Detector code
- sample_auth.log - Fake log for testing, 6 fails from 192.168.1.50, 1 fail from 10.0.0.5

## How to run

python3 main.py 2
python3 main.py 5
python3 main.py 10
python3 main.py

## Tests

- python3 main.py 2 -> ALERT, 6 > 2
- python3 main.py 5 -> ALERT, 6 > 5
- python3 main.py 10 -> No brute force, 6 is not > 10
- python3 main.py -> ALERT, uses default threshold 5

## How it works

- parse_log - Open log, loop lines, if Failed password in line, extract IP with regex, count per IP
- detect_brute_force - If count > threshold, flag as attacker
- main - Get threshold from terminal with sys.argv, default 5, print Evidence and ALERT

## Skills

Python, Regex, File handling, sys.argv, SOC log analysis
