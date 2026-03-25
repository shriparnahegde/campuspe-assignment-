import subprocess
import re

def get_arp_table(save_to_file=None):
    command = ["arp", "-a"]
    print("[*] Scanning local ARP table...\n")
    
    try:
        output = subprocess.check_output(command, stderr=subprocess.STDOUT, universal_newlines=True)
        
        # Regex to extract IP and MAC addresses
        pattern = re.compile(r"(\d{1,3}(?:\.\d{1,3}){3})\s+([0-9A-Fa-f]{2}[:-][0-9A-Fa-f]{2}[:-][0-9A-Fa-f]{2}[:-][0-9A-Fa-f]{2}[:-][0-9A-Fa-f]{2}[:-][0-9A-Fa-f]{2})")
        matches = pattern.findall(output)
        
        print(f"{'IP Address':<20} | {'MAC Address':<20}")
        print("-" * 45)
        
        for ip, mac in matches:
            # Standardize MAC address format
            mac_clean = mac.replace('-', ':')
            print(f"{ip:<20} | {mac_clean:<20}")
            
        print(f"\nTotal Devices Found: {len(matches)}")
        
        if save_to_file:
            with open(save_to_file, "w") as f:
                f.write(f"{'IP Address':<20} | {'MAC Address':<20}\n")
                f.write("-" * 45 + "\n")
                for ip, mac in matches:
                    f.write(f"{ip:<20} | {mac.replace('-', ':'):<20}\n")
            print(f"[+] Results successfully saved to {save_to_file}")
            
    except Exception as e:
        print(f"[-] Error retrieving ARP table: {e}")

if __name__ == "__main__":
    save_choice = input("Do you want to save the results to a text file? (y/n): ").strip().lower()
    filename = "arp_results.txt" if save_choice == 'y' else None
    get_arp_table(filename)