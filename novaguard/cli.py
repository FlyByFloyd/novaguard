import argparse
from novaguard.port_scan import scan_localhost
from novaguard.file_scan import scan_for_risky_files


def main():
    parser = argparse.ArgumentParser(
        description="NovaGuard v1 - simple local security scanner"
    )
    parser.add_argument("--ports", action="store_true", help="Run port scan")
    parser.add_argument("--files", action="store_true", help="Run risky file scan")
    parser.add_argument("--path", default=".", help="Path to scan (default: current folder)")

    args = parser.parse_args()

    # Default: if no flags are given, do both scans
    if not args.ports and not args.files:
        args.ports = True
        args.files = True

    print("NovaGuard v1 starting...\n")

    if args.ports:
        print("[Port Scan]")
        open_ports = scan_localhost()
        if open_ports:
            for port in open_ports:
                print(f"  - Port {port} is OPEN")
        else:
            print("  No common ports are open.")
        print()

    if args.files:
        print("[Risky File Scan]")
        scan = scan_for_risky_files(args.path)

        if scan["errors"]:
            for err in scan["errors"]:
                print(f"  Error: {err}")
        else:
            print(f"  Scanned files: {scan['scanned_files']}")
            print(f"  Risky files found: {scan['risky_count']}")
            if scan["risky_examples"]:
                print("  Examples:")
                for p in scan["risky_examples"]:
                    print(f"   - {p}")
            else:
                print("  No risky files found in the scanned path.")
        print()


if __name__ == "__main__":
    main()
