# Python TCP Port Scanner

A simple, fast, command-line port scanner used to detect open ports on a given host using multithreading to perform scans quickly and attempting basic banner grabbing to help identify services running on open ports. The only requirement is Python 3.x.

## Features

  -  Utilises `concurrent.futures` to scan multiple ports simultaneously.
  -  Attempts to identify the service on open ports by grabbing and displaying service banners
  -  Accepts both IP addresses and domain names (URLs).
  -  User is able to specify a single port or a custom range of ports to scan.
  -  If no port range is specified, the first 1024 ports are scanned.
  -  Robust error handling for invalid hostnames, malformed port ranges, incorrect arguments etc.

## Usage

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/BossOverlordX/Port-Scanner.git
    cd Port-Scanner
    ```

2.  **Run the script:**

    **Basic Scan (Default Ports 0-1024):**
    ```bash
    # USAGE: python3 port_scanner.py <targetIP/URL>
    # EXAMPLE:
    python3 port_scanner.py google.com
    ```

    **Custom Port Range Scan:**
    ```bash
    # USAGE: python3 port_scanner.py <targetIP/URL> <startPort-endPort>
    # EXAMPLE:
    python3 port_scanner.py 192.168.1.1 20-1000
    ```

## How It Works

The script parses all arguments using `sys.argv` and translates URLs into IPv4 addresses using `socket.gethostbyname()`.\
The script iterates through the provided port range, initialising a new thread for each that attempts to establish a connection using a TCP socket.\
If a connection is successful, the script then attempts basic banner grabbing by sending a generic HTTP GET request, printing the relevant response material alongside the port number (if receieved).

## Future Improvements
  -  **Verbose Mode:** Add a `-v` flag to show both open and closed ports for more detailed analysis.
  -  **Output to File:** Add a `-o` flag to save the scan results to a text file.

## ⚠️ Disclaimer

This tool is intended for educational purposes only and for use on systems where you have explicit permission.
