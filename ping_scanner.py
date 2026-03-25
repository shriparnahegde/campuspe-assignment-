import subprocess
import platform
import re

def ping_host(host):
    system_os = platform.system().lower()
    
    # Adapt command based on the OS
    if system_os == "windows":
        command = ["ping", "-n", "4", host]
    else:
        command = ["ping", "-c", "4", host]
        
    print(f"[*] Pinging {host}...")
    try:
        output = subprocess.check_output(command, stderr=subprocess.STDOUT, universal_newlines=True)
        
        # Extract average response time using regex
        if system_os == "windows":
            match = re.search(r"Average = (\d+ms)", output)
            avg_time = match.group(1) if match else "N/A"
        else:
            match = re.search(r"mdev = [\d\.]+/([\d\.]+)/", output)
            avg_time = match.group(1) + "ms" if match else "N/A"
            
        print(f"[+] {host} is ONLINE | Average Response Time: {avg_time}\n")
    except subprocess.CalledProcessError:
        print(f"[-] {host} is OFFLINE or blocking ping requests.\n")

if __name__ == "__main__":
    user_input = input("Enter IP addresses to ping (separated by commas): ")
    hosts = [h.strip() for h in user_input.split(",")]
    print("-" * 40)
    for h in hosts:
        ping_host(h)