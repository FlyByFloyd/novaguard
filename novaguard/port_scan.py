import socket

COMMON_PORTS = [
    21,   # FTP
    22,   # SSH
    23,   # Telnet
    25,   # SMTP
    80,   # HTTP
    443,  # HTTPS
    3389  # RDP
]

def scan_localhost(timeout=0.5):
    """
    Scan common ports on localhost.
    Returns a list of open ports.
    """
    open_ports = []

    for port in COMMON_PORTS:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)

        try:
            result = sock.connect_ex(("127.0.0.1", port))
            if result == 0:
                open_ports.append(port)
        except Exception:
            # Ignore errors and continue scanning
            pass
        finally:
            sock.close()

    return open_ports
