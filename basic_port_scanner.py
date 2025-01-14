import socket
import concurrent.futures
from datetime import datetime

def scan_port(host, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(1)  # Timeout for connection
            result = sock.connect_ex((host, port))

            if result == 0:
                if port == 80:
                    return f"Port {port}: HTTP service detected"
                elif port == 443:
                    return f"Port {port}: HTTPS service detected"
                elif port == 21:
                    return f"Port {port}: FTP service detected"
                elif port == 22:
                    return f"Port {port}: SSH service detected"
                elif port == 23:
                    return f"Port {port}: Telnet service detected"
                elif port == 25:
                    return f"Port {port}: SMTP service detected"
                elif port == 53:
                    return f"Port {port}: DNS service detected"
                elif port == 110:
                    return f"Port {port}: POP3 service detected"
                elif port == 143:
                    return f"Port {port}: IMAP service detected"
                else:
                    return f"Port {port}: Open"
            else:
                return f"Port {port}: Closed"
    except socket.timeout:
        return f"Port {port}: Timeout"
    except socket.error as e:
        return f"Error on port {port}: {e}"

def scan_ports(host, start_port, end_port):
    # Validate port range
    if start_port < 1 or end_port > 65535 or start_port > end_port:
        print("Invalid port range. Port numbers should be between 1 and 65535, and the start port should be less than or equal to the end port.")
        return
    
    print(f"\nStarting scan on {host} from port {start_port} to {end_port}\n")
    start_time = datetime.now()
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
        futures = [executor.submit(scan_port, host, port) for port in range(start_port, end_port + 1)]
        results = [future.result() for future in concurrent.futures.as_completed(futures)]
 
    # Print the results of the scan
    for result in results:
        print(result)

    end_time = datetime.now()
    total_time = end_time - start_time
    print(f"\nScanning completed in: {total_time}\n")

if __name__ == "__main__":
    try:
        host = input("Enter the target IP address or domain: ").strip()
        start_port = int(input("Enter the start port: "))
        end_port = int(input("Enter the end port: "))
        
        # Validate if the host is valid
        socket.gethostbyname(host)  

        scan_ports(host, start_port, end_port)
    except ValueError:
        print("Invalid input. Please enter a valid port number.")
    except socket.gaierror:
        print("Invalid IP address or domain name.")
