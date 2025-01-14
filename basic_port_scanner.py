import socket
import concurrent.futures
from datetime import datetime

def scan_port(host, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(1)  # You can adjust this timeout value if needed
            result = sock.connect_ex((host, port))
            if result == 0:
                return f"Port {port}: Open"
            else:
                return f"Port {port}: Closed"
    except socket.timeout:
        return f"Port {port}: Timeout"
    except socket.error as e:
        return f"Error on port {port}: {e}"

def scan_ports(host, start_port, end_port):
    if start_port < 1 or end_port > 65535 or start_port > end_port:
        print("Invalid port range. Port numbers should be between 1 and 65535, and the start port should be less than or equal to the end port.")
        return
    
    print(f"Starting scan on {host} from port {start_port} to {end_port}")
    start_time = datetime.now()
    
    # Using ThreadPoolExecutor to handle threading efficiently
    with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
        futures = [executor.submit(scan_port, host, port) for port in range(start_port, end_port + 1)]
        results = [future.result() for future in concurrent.futures.as_completed(futures)]

    # Print the results
    for result in results:
        print(result)

    end_time = datetime.now()
    total_time = end_time - start_time
    print(f"Scanning completed in: {total_time}")

if __name__ == "__main__":
    try:
        host = input("Enter the target IP address or domain: ").strip()
        start_port = int(input("Enter the start port: "))
        end_port = int(input("Enter the end port: "))
        
        # Validate that the host is a valid IP or domain
        socket.gethostbyname(host)  # Will raise an exception if the host is invalid

        scan_ports(host, start_port, end_port)
    except ValueError:
        print("Invalid input. Please enter a valid port number.")
    except socket.gaierror:
        print("Invalid IP address or domain name.")
