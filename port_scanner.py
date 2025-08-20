# Simple Python Port Scanner
# USAGE: python3 port_scanner.py <targetIP/URL> [targetPorts]
# EXAMPLE: python3 port_scanner.py google.com 80-443
# Default ports to scan are 0 to 1024

import socket
import sys
import os
import concurrent.futures

def port_connect(targetIP, port):
    # Create socket (IPv4, protocol TCP, time out after 0.5s)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)

    status = s.connect_ex((targetIP, port))
    if status == 0:
        # Try banner grabbing
        try:
            s.sendall(b'GET / HTTP/1.1\r\nHost: ' + targetIP.encode() + b'\r\n\r\n')
            banner = s.recv(1024).decode('utf-8', 'ignore').strip().splitlines()[0].split()[0]
            print(port, "---", banner)
        except:
            print(port)
        s.close()
        return 1
    s.close()
    return 0

# If no/too many arguments
if len(sys.argv) not in [2, 3]:
    print("Usage (default port values are 0-1024): python3 port_scanner.py <target IP/URL> [targetPorts]")
    print("Example: python3 port_scanner.py google.com 80-443")
    # Exit with status code 1 (error) - can be useful if this script is ran by another script
    sys.exit(1)

# Settings initialisation
if len(sys.argv) == 3:
    targetPorts = sys.argv[2]
else:
    print("No ports specified - using default: (0-1024)")
    targetPorts = "0-1024"
try:
    # Translate URLs to IPs (or keep IPs as they are)
    targetIP = socket.gethostbyname(sys.argv[1])

    parts = targetPorts.split("-")
    if len(parts) != 2:
        raise ValueError
    
    startPort = min(int(parts[0]), int(parts[1]))
    endPort = max(int(parts[0]), int(parts[1]))
    if not (0 <= startPort <= 65535 and 0 <= endPort <= 65535):
        print("Specified ports must be between 0 and 65535 inclusive")
        sys.exit(1)
# If gethostbyname() cannot resolve IP address
except socket.gaierror:
    print("URL couldn't be resolved to IP address")
    sys.exit(1)
except ValueError:
    print("Port argument was malformed (use the syntax startPort-endPort)")
    sys.exit(1)
except Exception as e:
    print(f"Unknown exception occured during initialisation of IP and port values:\n{e}")
    sys.exit(1)

# Define thread pool
pool = concurrent.futures.ThreadPoolExecutor(max_workers=2*os.cpu_count()+1)
futures = []

print(f"Open ports on IP {targetIP}:")
numOpen = 0

for i in range(startPort, endPort+1):
    # New thread for each port connection
    futures.append(pool.submit(port_connect, targetIP, i))

for future in concurrent.futures.as_completed(futures):
    numOpen += future.result()

pool.shutdown(wait=True)
print(f"\nTotal number of open ports between {startPort}-{endPort} on {sys.argv[1]}: {numOpen}")