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


print("\nIP")
input("1. Scan The Target Operating System For Open_Ports? (Y/N): 'Y/N' E.G., (1-65535): ")
input("2. Verify If There Are Any Potential Vulnerabilities In The Target Network? (Y/N): ")
input("3. Recon The Target IPs For Known Security Flaws? (Y/N): ")
input("4. Verify For Any Vulnerable Open_Ports In Target Operating Systems? (Y/N): ")
input("5. Exit? (Y/N): ")
print("Exiting...")
sys.exit(0)
