import subprocess
import shutil
import sys

# Check if Nmap is installed
if shutil.which("nmap") is None:
    print("[ERROR] Nmap is not installed.")
    
    # Ask the user if they want to install it
    choice = input("Do you want to install Nmap? (yes/no): ").strip().lower()
    
    if choice == "yes":
        # Detect OS
        if sys.platform == "win32":
            print("Installing Nmap using Chocolatey...")
            subprocess.run(["choco", "install", "nmap", "-y"], shell=True)
    else:
        print("Please install Nmap manually and rerun the script.")
        sys.exit(1)

else:
    ipconfig_output = subprocess.run(["ipconfig"], capture_output=True, text=True).stdout


    for line in ipconfig_output.split("\n"):    
        if "IPv4 Address" in line:
            user_ip = line.split(":")[-1].strip()
            break
    nmap_output = subprocess.run(["nmap", "-sV", user_ip], capture_output=True, text=True).stdout

    print(nmap_output)