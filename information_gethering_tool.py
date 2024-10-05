from scapy.all import ARP, Ether, srp
import socket

def scan_network(ip_range):
    
    arp_request = ARP(pdst=ip_range)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether/arp_request
    
   
    result = srp(packet, timeout=2, verbose=False)[0]

    
    devices = []
    
    for sent, received in result:
       
        devices.append({'ip': received.psrc, 'mac': received.hwsrc})
    
    return devices

def resolve_hostnames(devices):
    for device in devices:
        try:
            
            hostname = socket.gethostbyaddr(device['ip'])[0]
            device['hostname'] = hostname
        except socket.herror:
            device['hostname'] = None

def display_devices(devices):
    print("Discovered devices on the network:")
    print("IP Address\t\tMAC Address\t\tHostname")
    print("-" * 60)
    for device in devices:
        hostname = device['hostname'] if device.get('hostname') else 'N/A'
        print(f"{device['ip']}\t\t{device['mac']}\t\t{hostname}")

def main():
    ip_range = input("Enter the IP range (e.g., 192.168.1.0/24): ")
    
    print("Scanning the network...")
    devices = scan_network(ip_range)
    
    print("Resolving hostnames...")
    resolve_hostnames(devices)

    display_devices(devices)

if __name__ == "__main__":
    main()
