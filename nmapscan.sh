#!/bin/bash
# first step:
# Adding first the following alias and line to your ~/.zshrc
# nmapscan 
# alias nmapscan='/PATH/TO/THE/SCRIPT/./scan.sh'
# second step:
# update with source ~/.zshrc
# then execute as nmapscan and enter then just put the ip number
# and it will make the nmap scanning of all ports and services

echo "Target Ip:"
read ip_address

# Perform initial Nmap scan
echo "Starting all ports with Nmap..."
nmap -p- -open --min-rate 5000 -vvv -n -Pn $ip_address -oG allPorts

# Extract nmap information
function extractPorts() {
  ports="$(cat $1 | grep -oP '\d{1,5}/open' | awk '{print $1}' FS='/' | xargs | tr ' ' ',')"
  ip_address="$(cat $1 | grep -oP '\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}' | sort -u | head -n 1)"
  echo -e "\n[*] Extracting information...\n" > extractPorts.tmp
  echo -e "\t[*] IP Address: $ip_address"  >> extractPorts.tmp
  echo -e "\t[*] Open ports: $ports\n"  >> extractPorts.tmp
  echo $ports | tr -d '\n' | xclip -sel clip
  echo -e "[*] Ports copied to clipboard\n"  >> extractPorts.tmp
  cat extractPorts.tmp; rm extractPorts.tmp
}

# Call the extractPorts function with the generated output file
extractPorts allPorts

# Perform second Nmap scan using extracted information
echo "Scanning ports and services..."
nmap -sCV -p $ports $ip_address -oN targeted

echo "Completed."
