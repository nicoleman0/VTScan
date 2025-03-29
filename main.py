from scan import scan_url, get_url_report, get_api_key
from workbook import save_to_excel
from generate import generate_html_report
import argparse


def main():
    api_key = get_api_key()  # Get the API key from user input

    parser = argparse.ArgumentParser(description="Scan URLs with VirusTotal.")
    parser.add_argument(
        "urls",
        metavar="URL",
        type=str,
        nargs="+",
        help="URLs to scan (space-separated)",
    )
    args = parser.parse_args()
    urls = args.urls

    results = []
    for url in urls:
        scan_id = scan_url(url, api_key)  # Pass the API key to scan_url
        if scan_id:
            # Pass the API key to get_url_report
            report = get_url_report(scan_id, api_key)
            if report:
                stats = report.results.get('attributes', {}).get('stats', {})
                results.append({
                    'url': url,
                    'malicious': stats.get('malicious', 0),
                    'harmless': stats.get('harmless', 0),
                    'undetected': stats.get('undetected', 0)
                })

    save_to_excel(results)
    generate_html_report(results)


if __name__ == "__main__":
    main()
