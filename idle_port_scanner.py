import socket
import threading

# Set the target host and port range
target_host = '172.16.1.100'
start_port = 1
end_port = 65535
whitelist = [22, 80, 443]
open_ports = []
scan_counter = 1

# Define a function to scan a single port
def scan_port(port):
    # Skip ports in the whitelist
    if port in whitelist:
        return

    # Create a socket object
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.settimeout(0.5)

    # Try to connect to the target host and port
    try:
        response = client.connect((target_host, port))
        print(f"Port {port} is open!")
        open_ports.append(port)
        client.close()
    except:
        pass

# Scan open ports in the specified range using multiple threads
while True:
    for port in range(start_port, end_port+1):
        if port == end_port:
            if len(open_ports) == 0:
                print(f"Scan {scan_counter} report: No open ports detected outside the whitelist.")
            else:
                print(f"Scan {scan_counter} report: Detected open port(s): {open_ports}")
        thread = threading.Thread(target=scan_port, args=(port,))
        thread.start()

    # Wait for all threads to finish
    for thread in threading.enumerate():
        if thread != threading.current_thread():
            thread.join()
    scan_counter += 1
    open_ports = []
