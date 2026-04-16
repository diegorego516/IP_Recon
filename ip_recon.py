import os
import sys
import requests



BANNER = r"""
██╗██████╗     ██████╗ ███████╗ ██████╗ ██████╗ ███╗   ██╗
██║██╔══██╗    ██╔══██╗██╔════╝██╔════╝██╔═══██╗████╗  ██║
██║██████╔╝    ██████╔╝█████╗  ██║     ██║   ██║██╔██╗ ██║
██║██╔═══╝     ██╔══██╗██╔══╝  ██║     ██║   ██║██║╚██╗██║
██║██║         ██║  ██║███████╗╚██████╗╚██████╔╝██║ ╚████║
╚═╝╚═╝         ╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝
		[ IP RECON V3 - BY DIEGODEV ]
"""

print(BANNER)

print("\nIP Recon Menu")
options = input("1. Recon The Target IP? (Y/N): ")
options = input("2. Scan The Target IP For Open_Ports? (Y/N): ")
options = input("3. Verify Target IP For Vulnerabilities? (Y/N): ")
options = input("4. Check IF there IS Any Vulnerabilities In The Target IP? (Y/N): ")
options = input("5. Exit? (Y/N): ")
sys.exit(0)
print("Exiting...")

print("\nIP Recon Options Menu")
options = input("1. Scan The Target IP? (Y/N): ")
options = input("2. Verify If There Are Any Vulnerabilities In The Target Operating Systems, E.G 'Windows11', 'Mac OS X 18.6', 'Android-X86_64'? (Y/N): ")
options = input("3. Analyze For Any Potential Vulnerabilities In The Target Networks? (Y/N): ")
options = input("4. Generate A Concise, Convincing And Promissing Well Detailed Bug Bounty Report Document? (Y/N): ")
options = input("5. Exit? (Y/N): ")
sys.exit(0)
print("Exiting...")

