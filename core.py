import vt
import time

API_KEY = "your_api_key"


def scan_url(url):
    with vt.Client(API_KEY) as client:
        try:
            url_id = vt.url_id(url)
            analysis = client.scan_url(url_id)
            print(f"Scanning URL: {url} ID: {analysis.id}")
            return analysis.id
        except Exception as e:
            print(f"Error scanning URL: {url} - {e}")
            return None


def get_url_report(scan_id):
    with vt.Client(API_KEY) as client:
        try:
            analysis = client.get_object(f"/analyses/{scan_id}")
            while analysis.status != "completed":
                print("Waiting for results...")
                time.sleep(5)
                analysis = client.get_object(f"/analyses/{scan_id}")
            return analysis
        except Exception as e:
            print(f"Error fetching report: {e}")
            return None
