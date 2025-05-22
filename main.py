import argparse
from log_parser import parse_logs
from alerts import check_brute_force
from visualizer import plot_attempts
from report_gen import generate_html_report

def main():
    parser = argparse.ArgumentParser(description="IRSim Log Monitor")
    parser.add_argument("--logfile", required=True)
    parser.add_argument("--threshold", type=int, default=3)
    parser.add_argument("--report", action="store_true")
    args = parser.parse_args()

    logs = parse_logs(args.logfile)
    alerts = check_brute_force(logs, threshold=args.threshold)

    print("\n=== ALERTS ===")
    for ip, count in alerts:
        print(f"[!] {ip} - {count} failed login attempts")

    print("\nGenerating chart...")
    plot_attempts(logs)

    if args.report:
        generate_html_report(logs)
        print("Report generated: report.html")

if __name__ == "__main__":
    main()
