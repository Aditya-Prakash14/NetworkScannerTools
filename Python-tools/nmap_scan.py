import nmap

def scan_target(target):
    nm = nmap.PortScanner()
    nm.scan(target, arguments='-p- -sV')
    return nm

def display_results(nm):
    for host in nm.all_hosts():
        print(f"\nHost: {host} ({nm[host].hostname()})")
        print(f"State: {nm[host].state()}")
        for proto in nm[host].all_protocols():
            print(f"\nProtocol: {proto}")
            for port in sorted(nm[host][proto].keys()):
                state = nm[host][proto][port]['state']
                service = nm[host][proto][port]['name']
                version = nm[host][proto][port].get('version', 'N/A')
                print(f"Port: {port}\tState: {state}\tService: {service}\tVersion: {version}")

def main():
    target = input("Enter the target IP or hostname: ")
    nm = scan_target(target)
    display_results(nm)

if __name__ == "__main__":
    main()
