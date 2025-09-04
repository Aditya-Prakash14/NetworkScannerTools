#!/bin/bash

LOG_DIR="$HOME/wifi-logs"
mkdir -p "$LOG_DIR"

SSID=$(nmcli -t -f active,ssid dev wifi | egrep '^yes' | cut -d: -f2)
DATE=$(date '+%Y-%m-%d_%H-%M-%S')
LOG_FILE="$LOG_DIR/${SSID}_$DATE.log"

echo "📡 WiFi Recon Report - $SSID ($DATE)" > "$LOG_FILE"
echo "----------------------------------" >> "$LOG_FILE"

# WiFi Info
echo -e "\n📶 WiFi Information:" >> "$LOG_FILE"
nmcli -f SSID,BSSID,FREQ,CHAN,RATE,SIGNAL,SECURITY dev wifi list | grep "$SSID" >> "$LOG_FILE"

# Network Info
echo -e "\n🌐 Network Info:" >> "$LOG_FILE"
echo "Local IP: $(hostname -I | awk '{print $1}')" >> "$LOG_FILE"
echo "Gateway: $(ip route | grep default | awk '{print $3}')" >> "$LOG_FILE"
echo "Public IP: $(curl -s ifconfig.me)" >> "$LOG_FILE"

# Connected Devices (IP + MAC)
echo -e "\n👥 Connected Devices:" >> "$LOG_FILE"
sudo arp-scan --localnet | tee -a "$LOG_FILE"

# Resolve Hostnames
echo -e "\n🔎 Hostnames:" >> "$LOG_FILE"
for ip in $(arp -a | awk '{print $2}' | sed 's/[()]//g'); do
    host $ip | tee -a "$LOG_FILE"
done

# Port Scan (each device)
echo -e "\n🛡️ Port Scan (Top 1000 ports):" >> "$LOG_FILE"
for ip in $(arp -a | awk '{print $2}' | sed 's/[()]//g'); do
    echo -e "\nScanning $ip ..." >> "$LOG_FILE"
    nmap -sV --top-ports 1000 $ip >> "$LOG_FILE"
done

echo "✅ Report saved: $LOG_FILE"

