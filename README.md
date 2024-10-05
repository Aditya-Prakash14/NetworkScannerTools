# Network Tools

A collection of Python scripts for various network-related tasks. These tools can assist in network scanning, information gathering, and penetration testing.

## Tools

- **arp_scan.py**: This script scans the local network for active devices using the Address Resolution Protocol (ARP). It lists IP and MAC addresses, allowing you to identify devices on your network.
- **information_gathering_tool.py**: This tool collects various details about a target system or network, including open ports, service versions, and DNS information, helping in reconnaissance during penetration testing.
- **ip_scan.py**: This script performs a basic ping sweep across a specified range of IP addresses to identify which hosts are up and responding to requests.
- **network_fuzzer.py**: This tool sends a variety of packets to a target service to discover potential vulnerabilities. It can be useful for testing the robustness of network services.
- **nmap_scan.py**: This script interfaces with Nmap, a powerful network scanning tool, to perform comprehensive scans of target hosts, gathering detailed information on open ports and services.

## Installation

To run these scripts, you need Python installed. You can download it from [python.org](https://www.python.org/downloads/). Additionally, some tools may require external libraries or tools, such as Nmap. Install the required libraries using pip:

```bash
pip install scapy
pip install python-nmap
