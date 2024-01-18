import socket
import threading


def scan_port(ip, port, open_ports):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        sock.connect((ip, port))
        open_ports.append(port)
    except (socket.timeout, socket.error):
        pass
    finally:
        sock.close()


def scan_range(start_ip, end_ip):
    results = []
    start_ip_parts = list(map(int, start_ip.split('.')))
    end_ip_parts = list(map(int, end_ip.split('.')))

    for a in range(start_ip_parts[0], end_ip_parts[0] + 1):
        for b in range(start_ip_parts[1], end_ip_parts[1] + 1):
            for c in range(start_ip_parts[2], end_ip_parts[2] + 1):
                for d in range(start_ip_parts[3], end_ip_parts[3] + 1):
                    ip = f"{a}.{b}.{c}.{d}"
                    open_ports = []

                    threads = []
                    for port in range(1, 1025):
                        thread = threading.Thread(
                            target=scan_port, args=(ip, port, open_ports))
                        threads.append(thread)
                        thread.start()

                    for thread in threads:
                        thread.join()

                    if open_ports:
                        results.append(
                            f"{ip}: ({', '.join(map(str, open_ports))}) are open")

    return results
