import socket

COMMON_SERVICES = {
    21: "FTP",
    22: "SSH",
    80: "HTTP",
    443: "HTTPS",
    8080: "HTTP-ALT"
}

def port_scan(target, ports):
    print("\n[+] Port Scanning Started")
    open_count = 0

    for port in ports:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((target, port))

            if result == 0:
                service = COMMON_SERVICES.get(port, "Unknown")
                print(f"[OPEN] Port {port} ({service})")
                open_count += 1

            sock.close()
        except Exception:
            pass

    print(f"\nScan completed. Open ports found: {open_count}")
