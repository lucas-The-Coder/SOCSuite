import socket
import sys


def scan_port(host, port):

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    sock.settimeout(1)

    result = sock.connect_ex((host, port))

    if result == 0:
        return True
    else:
        return False

    sock.close()


def scan_host(host):
    ports = [21, 22, 80, 443, 3306, 5432, 8000]
    open_ports = []

    for port in ports:
        result = scan_port(host, port)
        if result is True:
            open_ports.append(port)
            print(port, "OPEN")
        else:
            print(port, "CLOSED")

    return open_ports


def main():
    host = "127.0.0.1"
    open_ports = scan_host(host)

    print(open_ports)


if __name__ == "__main__":
    main()
