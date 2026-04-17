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


print("\nIP Recon Options Menu")
input("1. Scan The Target Operating System For Open_Ports? (Y/N): 'Y/N' E.G., (1-65535): ")
input("2. Verify If There Are Any Potential Vulnerabilities In The Target Network? (Y/N): ")
input("3. Recon The Target IPs For Known Security Flaws? (Y/N): ")
input("4. Verify For Any Vulnerable Open_Ports In Target Operating Systems? (Y/N): ")
input("5. Exit? (Y/N): ")
print("Exiting...")


HOST = "127.0.0.1"
PORT = 5000

input("Scan the target Operating System For Open_Ports (1-65535): ")
input("Do you Want to scan the target operating system for open_ports: (Y/N?): ")
choice = input == "Y"
input("Starts the scan on the target operating system for vulnerable open_ports: ")
print("Finished scanning, No vulnerabilities found.")
