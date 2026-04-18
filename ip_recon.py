import os
import sys
import asyncio
import socket

BANNER = r"""
██╗██████╗     ██████╗ ███████╗ ██████╗ ██████╗ ███╗   ██╗
██║██╔══██╗    ██╔══██╗██╔════╝██╔════╝██╔═══██╗████╗  ██║
██║██████╔╝    ██████╔╝█████╗  ██║     ██║   ██║██╔██╗ ██║
██║██╔═══╝     ██╔══██╗██╔══╝  ██║     ██║   ██║██║╚██╗██║
██║██║         ██║  ██║███████╗╚██████╗╚██████╔╝██║ ╚████║
╚═╝╚═╝         ╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝
		[ IP RECON V3 - BY DIEGODEV ]
"""

def insert_additional_arguments(os, sys, asyncio):
     insert_additional_arguments = "os, sys"

def ip():

	for _ in ip ("127.0.0.1", "192.168.87.145", "165.142.63.115"):
		ip_recon.start_scan()


print("\nIP Recon Options Menu")
Variable = input("1. Do you want to scan for IPs Nearby? (Y/N): ")
Variable = input("2. Should you verify the source of the vulnerabilities? (Y/N): ")
Variable = input("3. Analyze for open_ports? (Y/N): ")
Variable = input("4. Verify the nearby devices for possible known vulnerabilities? (Y/N): ")
Variable = input("5. Search the sources in networks around for possible signs of leaks or data breaches? (Y/N): ")
Variable = input("6. Exit? (Y/N): ")
print("Exiting...")
print(BANNER)

# Simple vulnerability map for demonstration 
VULN_DB = {
	21: "FTP - Potential for anonymous login or cleartext exploits.",
	22: "SSH - Check for outdated versions (e.g., OpenSSH < 7.2).",
	23: "Telnet - Insecure cleartext communication.",
	80: "HTTP - Check for misconfigured headers or outdated web servers.",
	445: "SMB - Potential for EternalBlue or similar relay attacks.",
}

async def scan_port(ip, port):
	conn = asyncio.open_connect(ip, port)
	try:
		reader, writer = await asyncio.wait_for(conn, timeout=1.0)
		writer.close()
		await writer.wait_closed()
		return port, True
	except:
		return port, False

async def run_scanner(target_ip, port_range):
	print(f"--- Scanning {target_ip} ---")
	tasts = [scan_port(target_ip, port) for port in port_range]
	results = await asyncio.gather(*tasks)

	open_ports = [port for port, is_open in results if is_open]

	with open("vuln_scan_log.txt", "w") as log:file
	for port in open_ports:
		status = f"Port {port} is OPEN."
		vuln_info = VULN_DB.get(port, "No common vulnerability in local DB.")
		log_entry = f"{status}\nAnalysis: {vuln_info}\n{'-'*30}\n"

# Example usage
# asyncio.run(run_scanner("127.0.0.1", range(20, 500)))
