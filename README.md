# campuspe-assignment-
Python scripts using subprocess and regex to automate Ping, ARP, and Nmap scans.
# Network Scanning Tools - Automation Project

Assignment - 2 
Author: Shriparna PRaveenkumar Hegde 

 Overview
For this assignment, I built three Python tools to automate common network reconnaissance tasks. The goal was to use Python's `subprocess` module to run system commands like Ping and ARP, and then use Regular Expressions (`re`) to clean up the output into readable tables.

 1. Ping Scanner (`ping_scanner.py`)
This tool checks if a list of hosts is online.
* Features: It handles both single IPs and multiple hosts (separated by commas).
* Platform: I've tested this on Kali Linux, but it's built to work on Windows and Mac too by checking the OS type before sending the command.
* Data: It pulls out the average response time (ms) so you can see how fast the connection is.

2. ARP Scanner (`arp_scanner.py`)
This script looks at the local ARP table to see which devices are currently mapped to your network.
* Output: It displays a clean table of IP addresses and their matching MAC addresses.
* Bonus: I included a total count of entries and an option to save the results to a text file.

 3. Nmap Scanner (`nmap_scanner.py`)
A more advanced tool that acts as a wrapper for Nmap.
* Safety: It first checks if Nmap is even installed on your system before trying to run.
* Functionality: You can choose between a simple host discovery scan, a port scan, or even OS and service detection.
* Reliability: It uses timeout handling so the script doesn't hang forever on a slow network.



 Setting Up
To run these scripts, you'll need **Python 3.6+** and **Nmap** installed.

On Kali Linux / Debian / Ubuntu:
```bash
sudo apt update
sudo apt install nmap net-tools python3
