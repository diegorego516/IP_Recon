# IP Recon

An authorization-first TCP port scanner for one host at a time. It checks
whether ports accept TCP connections; it does not exploit services or identify
vulnerabilities.

Only scan systems you own or have explicit permission to test.

## Usage

```bash
python ip_recon.py 127.0.0.1 -p 22,80,443
python ip_recon.py example.test -p 1-1024 --timeout 0.5 --output report.txt
```

Port specifications may contain comma-separated ports and inclusive ranges.
