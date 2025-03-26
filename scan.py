import vt
import time
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('VT_API_KEY')
if not API_KEY:
    raise ValueError(
        "API key not found. Please create a .env file with VT_API_KEY=<your_api_key>")


def scan_url(url):
    """Scan a URL using VirusTotal API."""
    with vt.Client(API_KEY) as client:
        try:
            analysis = client.scan_url(url)
            print(f"Scanning URL: {url} | Analysis ID: {analysis.id}")
            return analysis.id
        except Exception as e:
            print(f"Error scanning URL: {url} - {e}")
            return None


def get_url_report(scan_id):
    """Get the report for a given analysis ID."""
    with vt.Client(API_KEY) as client:
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
