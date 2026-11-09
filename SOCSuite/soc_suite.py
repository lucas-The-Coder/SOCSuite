import subprocess


def run_tool(name, command):
    result = subprocess.run(command, capture_output=True, text=True)

    output = result.stdout

    print("=== " + name + " === \n")
    print("=== " + output + " ===")

    return output


def main():
    print("SOC Suite | Starting Full Scan")

    run_tool("BruteGuard", ["python3", "BruteGuard/main.py", "2"])

    run_tool("PortSentinel", ["python3", "PortSentinel/scanner.py"])

    run_tool(
        "FileSentinel",
        ["python3", "FileSentinel/monitor.py", "FileSentinel/test_folder", "check"],
    )

    run_tool(
        "IOCSentinel", ["python3", "IOCSentinel/checker.py", "IOCSentinel/iocs.txt"]
    )

    print("SOC Suite | Scan Complete")


if __name__ == "__main__":
    main()
