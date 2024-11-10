import nmap
import json

def scan_ports(target, port):
    nm = nmap.PortScanner()

    print(f"Scanning {target} on port {port}...")

    nm.scan(target, str(port))  

    scan_results = {}

    if target in nm.all_hosts():
        scan_results['host'] = target
        scan_results['open_ports'] = []

        for protocol in nm[target].all_protocols():
            ports = nm[target][protocol].keys()

            for p in ports:
                if nm[target][protocol][p]['state'] == 'open':
                    port_info = {
                            'port': p,
                            'protocol': protocol,
                            'name': nm[target][protocol][p].get('name', 'unknown')
                            }
                    scan_results['open_ports'].append(port_info)
        if not scan_results['open_ports']:
            scan_results['open_ports'] = 'No open ports found'
    return scan_results

#Calling scan_ports function
target = '127.0.0.1'
port = 3000

# Open a file in write mode
print("Port Scan results for" + target + "on port" + str(port))
print(scan_ports(target, port))

