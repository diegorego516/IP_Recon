#!/usr/bin/env python3
"""Small, authorization-first TCP port scanner.

Only scan hosts and ports that you own or have explicit permission to test.
This tool performs connection checks; it does not exploit services or test
for vulnerabilities.
"""

from __future__ import annotations

import argparse
import asyncio
import contextlib
import ipaddress
import socket
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


BANNER = r"""
██╗██████╗     ██████╗ ███████╗ ██████╗ ██████╗ ███╗   ██╗
██║██╔══██╗    ██╔══██╗██╔════╝██╔════╝██╔═══██╗████╗  ██║
██║██████╔╝    ██████╔╝█████╗  ██║     ██║   ██║██╔██╗ ██║
██║██╔═══╝     ██╔══██╗██╔══╝  ██║     ██║   ██║██║╚██╗██║
██║██║         ██║  ██║███████╗╚██████╗╚██████╔╝██║ ╚████║
╚═╝╚═╝         ╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝
                [ IP RECON V3 ]
"""


@dataclass(frozen=True)
class ScanResult:
    port: int
    is_open: bool


def parse_ports(spec: str) -> list[int]:
    """Parse comma-separated ports and inclusive ranges."""
    ports: set[int] = set()
    for item in spec.split(","):
        item = item.strip()
        if not item:
            continue
        if "-" in item:
            start_text, end_text = item.split("-", 1)
            try:
                start, end = int(start_text), int(end_text)
            except ValueError as exc:
                raise argparse.ArgumentTypeError(f"invalid port range: {item}") from exc
            if start > end:
                raise argparse.ArgumentTypeError(f"port range is reversed: {item}")
            ports.update(range(start, end + 1))
        else:
            try:
                ports.add(int(item))
            except ValueError as exc:
                raise argparse.ArgumentTypeError(f"invalid port: {item}") from exc

    if not ports or any(port < 1 or port > 65535 for port in ports):
        raise argparse.ArgumentTypeError("ports must be between 1 and 65535")
    return sorted(ports)


def validate_target(target: str) -> str:
    """Reject empty targets and CIDR ranges; this tool scans one host at a time."""
    if not target.strip():
        raise argparse.ArgumentTypeError("target cannot be empty")
    try:
        if "/" in target:
            ipaddress.ip_network(target, strict=False)
            raise argparse.ArgumentTypeError("CIDR ranges are not supported; provide one host")
        ipaddress.ip_address(target)
    except ValueError:
        try:
            socket.getaddrinfo(target, None, type=socket.SOCK_STREAM)
        except socket.gaierror as exc:
            raise argparse.ArgumentTypeError(f"could not resolve target: {target}") from exc
    return target


async def scan_port(target: str, port: int, timeout: float) -> ScanResult:
    """Attempt one TCP connection and close it immediately if successful."""
    try:
        reader, writer = await asyncio.wait_for(
            asyncio.open_connection(target, port), timeout=timeout
        )
    except (asyncio.TimeoutError, OSError):
        return ScanResult(port, False)

    writer.close()
    with contextlib.suppress(Exception):
        await writer.wait_closed()
    return ScanResult(port, True)


async def run_scanner(
    target: str,
    ports: Iterable[int],
    timeout: float = 1.0,
    concurrency: int = 100,
) -> list[ScanResult]:
    """Scan ports on one target, limiting concurrent connection attempts."""
    semaphore = asyncio.Semaphore(concurrency)

    async def limited_scan(port: int) -> ScanResult:
        async with semaphore:
            return await scan_port(target, port, timeout)

    return await asyncio.gather(*(limited_scan(port) for port in ports))


def write_log(path: Path, target: str, results: Iterable[ScanResult]) -> None:
    """Write a simple report containing open ports."""
    open_ports = [result.port for result in results if result.is_open]
    with path.open("w", encoding="utf-8") as log:
        log.write(f"Target: {target}\n")
        log.write("Open ports: " + (", ".join(map(str, open_ports)) or "none") + "\n")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Check TCP ports on one host that you are authorized to test."
    )
    parser.add_argument("target", type=validate_target, help="hostname or IP address")
    parser.add_argument(
        "-p",
        "--ports",
        type=parse_ports,
        default=parse_ports("1-1024"),
        help="ports, comma-separated and/or ranges (default: 1-1024)",
    )
    parser.add_argument("--timeout", type=float, default=1.0, help="per-port timeout in seconds")
    parser.add_argument(
        "--concurrency", type=int, default=100, help="maximum simultaneous connections"
    )
    parser.add_argument("-o", "--output", type=Path, help="optional report file")
    return parser


async def async_main(args: argparse.Namespace) -> int:
    if args.timeout <= 0 or args.concurrency <= 0:
        raise ValueError("timeout and concurrency must be greater than zero")

    print(f"Scanning {args.target} ({len(args.ports)} ports)...")
    results = await run_scanner(args.target, args.ports, args.timeout, args.concurrency)
    open_ports = [result.port for result in results if result.is_open]
    print("Open ports: " + (", ".join(map(str, open_ports)) or "none"))
    if args.output:
        write_log(args.output, args.target, results)
        print(f"Report written to {args.output}")
    return 0


def main() -> int:
    args = build_parser().parse_args()
    try:
        return asyncio.run(async_main(args))
    except ValueError as exc:
        print(f"error: {exc}", flush=True)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
