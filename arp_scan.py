import scapy.all as scapy

def scan_network(ip_range):
    arp_request = scapy.ARP(pdst=ip_range)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    
    clients = []
    for element in answered_list:
        client_dict = {"ip": element[1].psrc, "mac": element[1].hwsrc}
        clients.append(client_dict)
    
    return clients

ip_range = "10.5.63.0/24"
clients = scan_network(ip_range)

for client in clients:
    print(f"IP: {client['ip']}, MAC: {client['mac']}")