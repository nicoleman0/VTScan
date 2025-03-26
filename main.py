from scan import scan_url, get_url_report
from workbook import save_to_excel
from generate import generate_html_report


def main():
    urls = [
        "example.com",
        "malware.com"
        # Add more URLs here
    ]

    results = []
    for url in urls:
        scan_id = scan_url(url)
        if scan_id:
            report = get_url_report(scan_id)
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
