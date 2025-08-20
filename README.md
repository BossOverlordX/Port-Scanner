# Python TCP Port Scanner

A simple, command-line port scanner, that can be used to detect open ports on a given IP/URL. Only requirement is having Python 3.x installed :D

## Features

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

The script parses all arguments using sys.argv and translates URLs into IPv4 addresses using socket.gethostbyname().
The script iterates through the provided port range, attempting to establish a connection for each port using a TCP socket.
Using socket.connect_ex(), the script will be able to only output ports with a successful status code and will not raise exceptions for failed connections.

## Future Improvements
  -  **Threading:** Implement multithreading to perform multiple port checks concurrently.
  -  **Banner Grabbing:** Add functionality to retrieve service banners from open ports to identify the running services.
  -  **Verbose Mode:** Add a `-v` flag to show both open and closed ports for more detailed analysis.

## ⚠️ Disclaimer

This tool is intended for educational purposes only and for use on systems where you have explicit permission.
