import re
import sys
import os


def parse_log(file_path):
    ip_counts = {}

    f = open(file_path, "r")

    for line in f:
        if "Failed password" in line:
            match = re.search(r"\d+\.\d+\.\d+\.\d+", line)
            ip = match.group(0)

            if ip not in ip_counts:
                ip_counts[ip] = 0

            ip_counts[ip] += 1

    return ip_counts


def detect_brute_force(ip_counts, threshold):
    attackers = []

    for ip, count in ip_counts.items():
        if count > threshold:
            attackers.append(ip)

    return attackers


def main():
    ip_counts = parse_log(os.path.join(os.path.dirname(__file__), "sample_auth.log"))

    if len(sys.argv) > 1:
        threshold = int(sys.argv[1])
    else:
        threshold = 5

    attackers = detect_brute_force(ip_counts, threshold)

    if attackers:
        print("ALERT", ip_counts)
    else:
        print("No brute for detected", ip_counts)


if __name__ == "__main__":
    main()
