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
input("1. Scan The Target Operating System For Open_Ports? E.G., (1-65535): ")
input("2. Verify If There Are Any Potential Vulnerabilities In The Target Network? (Y/N): ")
input("3. Recon The Target IPs For Known Security Flaws? (Y/N): ")
input("4. Verify For Any Vulnerable Open_Ports In Target Operating Systems? (Y/N): ")
input("5. Exit? (Y/N): ")
print("Exiting...")


HOST = "142.127.45.105", "192.168.87.145", "168.145.62.127"
PORT = "80, 21, 22" 

Variable = input("Scan the target Operating System For Open_Ports (1-65535): ")
Variable = input("Do you Want to scan the target operating system for open_ports: (Y/N?): ")
choice = input == "Y"
Variable = input("Starts the scan on the target operating system for vulnerable open_ports? (Y/N): ")
print("Finished scanning, No vulnerabilities found.")

print("\nInitializing IP Recon Framework Menu...")
Variable = input("1. Start the scanning for vulnerable devices nearby? (Y/N): ")
Variable = input("2. Verify the range in local networks for possible known vulnerabilities and sofisticated cyber threat signatures? (Y/N): ")
Variable = input("3. Analyze the networks for open ports and determine if they're really vulnerable or not? (Y/N): ")
Variable = input("4. Recon the networks for any case of incidents involving computer hacking signs or such illegal activities? (Y/N): ")
Variable = input("5. Exit? (Y/N): ")
print("Exiting...")

print("\nStarting The IP Recon Modules Menu")
Variable = input("1. Start the IP Reconnainsance for IP Mapping? (Y/N): ")
Variable = input("2. Verify the Open_Ports for any vulnerabilities? (Y/N): ")
Variable = input("3. Analyze the Open_Ports for any case of data breaches or any incidents involving cyber attacks? (Y/N): ")
Variable = input("4. Recon the IP Addresses for any incidents in nearby devices or PCs? (Y/N): ")
Variable = input("5. Exit? (Y/N): ")
print("Exiting...")

def ip_recon():

	ip_recon.scan(HOST, PORT)
