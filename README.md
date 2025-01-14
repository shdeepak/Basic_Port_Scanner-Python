# Basic_Port_Scanner-Python

A simple and efficient Python-based tool for scanning a range of ports on a specified host. This script uses multithreading to quickly determine whether specific ports on a target system are open or closed. It is designed to be a lightweight solution for network administrators, security enthusiasts, and anyone who needs to check the availability of open ports of an IP address.

## Features

- **Multithreaded Scanning**: Scans multiple ports simultaneously to speed up the process.
- **Port Range**: Allows scanning a range of ports, giving flexibility in the number of ports to check.
- **Open/Closed Status**: Reports whether each scanned port is open or closed, helping identify which services are available.
- **Simple Interface**: The script uses basic command-line inputs, making it easy to use without complicated setup.

## Use Cases

- **Network Security**: Identify open ports that could be potential security vulnerabilities.
- **Service Monitoring**: Verify the status of network services by scanning specific ports on remote servers.

## Requirements

- Python 3.x

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/shdeepak/Basic_Port_Scanner-Python.git
    cd Basic_Port_Scanner-Python
    ```
    
2. Run the port scanner:
    ```bash
    python basic_port_scanner.py
    ```

## Usage

After running the script, it will prompt you for the following inputs:

1. **Host**: The target IP address or domain name you want to scan.
2. **Start Port**: The first port in the range to begin scanning.
3. **End Port**: The last port in the range to stop scanning.

### Example:

```bash
    $ python port_scanner.py
    Enter the target IP address or domain: 192.168.1.1
    Enter the start port: 20
    Enter the end port: 1024
