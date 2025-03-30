Automating Nmap Scan
Overview
This script automates the process of running an Nmap scan by first checking if Nmap is installed. If Nmap is not found, it prompts the user to install it. Once installed, the script retrieves the system's IPv4 address and performs a service version scan (-sV) on the detected IP, displaying the results.

Features
Automatically checks for Nmap installation

Guides the user through installation if missing

Retrieves the system’s IPv4 address

Runs an Nmap service version scan on the detected IP

Displays the scan results in the terminal

Installation & Usage
To use this script, ensure Python is installed on your system. Running the script will check for Nmap, prompt for installation if necessary, and then proceed with scanning.
