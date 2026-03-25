import subprocess
import shutil
import sys

def check_nmap_installed():
    if not shutil.which("nmap"):
        print("[-] Error: Nmap is not installed or not in your system PATH.")
        print("[*] Please install it first (e.g., 'sudo apt install nmap' on Linux).")
        sys.exit(1)

def run_nmap_scan(target, scan_type):
    # Mapping user choices to Nmap flags
    scan_options = {
        "1": "-sn",        # Simple Host Discovery (Ping scan)
        "2": "-p 1-1000",  # Scan first 1000 ports
        "3": "-A"          # Aggressive scan: OS and service detection
    }
    
    flag = scan_options.get(scan_type, "-sn")
    command = ["nmap", flag, target]
    
    print(f"\n[*] Executing: {' '.join(command)}")
    try:
        # 60-second timeout to prevent infinite hanging
        result = subprocess.run(command, capture_output=True, text=True, timeout=60)
        print("\n--- Scan Results ---")
        print(result.stdout)
    except subprocess.TimeoutExpired:
        print("[-] Scan timed out after 60 seconds. The network might be too slow or the host is unresponsive.")
    except Exception as e:
        print(f"[-] An unexpected error occurred: {e}")

if __name__ == "__main__":
    check_nmap_installed()
    
    target_ip = input("Enter target IP or Domain (e.g., 192.168.1.1 or scanme.nmap.org): ")
    
    print("\nSelect Scan Type:")
    print("1. Host Discovery (Check if online)")
    print("2. Port Scan (Top 1000 ports)")
    print("3. Advanced OS and Service Detection")
    choice = input("\nEnter choice (1/2/3): ").strip()
    
    run_nmap_scan(target_ip, choice)