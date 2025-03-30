import typer
from typing_extensions import Annotated
from scan import scan_url, get_url_report, get_api_key
from workbook import save_to_excel
from generate import generate_html_report

app = typer.Typer()


@app.command()
def main(
    urls: Annotated[
        list[str],
        typer.Argument(help="URLs to scan (space-separated)"),
    ],
    api_key: Annotated[
        str,
        typer.Option(
            "--api-key",
            "-k",
            help="Your VirusTotal API key. If not provided, you will be prompted.",
        ),
    ] = None,
):
    """
    Scan URLs with VirusTotal and generate reports.
    """
    if not api_key:
        api_key = get_api_key()

    results = []
    for url in urls:
        scan_id = scan_url(url, api_key)
        if scan_id:
            report = get_url_report(scan_id, api_key)
            if report:
                attributes = report.get("attributes", {})
                stats = attributes.get("stats", {})
                results.append(
                    {
                        "url": url,
                        "malicious": stats.get("malicious", 0),
                        "harmless": stats.get("harmless", 0),
                        "undetected": stats.get("undetected", 0),
                    }
                )
            else:
                print(f"No report found for {url}")
        else:
            print(f"Scan failed for {url}")

    if results:
        save_to_excel(results)
        generate_html_report(results)
    else:
        print("No results to report.")


if __name__ == "__main__":
    app()
