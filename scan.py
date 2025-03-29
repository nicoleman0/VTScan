import vt
import time


def get_api_key():
    api_key = input("Please enter your VirusTotal API key: ")
    if not api_key:
        raise ValueError("API key cannot be empty.")
    return api_key


def scan_url(url, api_key):
    with vt.Client(api_key) as client:
        try:
            analysis = client.scan_url(url)
            print(f"Scanning URL: {url} | Analysis ID: {analysis.id}")
            return analysis.id
        except Exception as e:
            print(f"Error scanning URL: {url} - {e}")
            return None


def get_url_report(scan_id, api_key):
    """Get the report for a given analysis ID."""
    with vt.Client(api_key) as client:
        try:
            while True:
                analysis = client.get_object(f"/analyses/{scan_id}")
                if analysis.status == "completed":
                    print("Analysis completed.")
                    return analysis
                print("Waiting for results... Retrying in 10 seconds.")
                time.sleep(10)
        except Exception as e:
            print(f"Error fetching report: {e}")
            return None
