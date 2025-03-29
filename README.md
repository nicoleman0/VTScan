# VTScan: VirusTotal URL Scanner and Reporting Tool

VTScan - a simple Python-based command-line tool designed to scan URLs using the VirusTotal API, collect scan results, and generate both Excel and HTML reports. Its purpose is to streamline the process of checking multiple URLs for potential threats.

## Prerequisites

*   **Python 3.x:** Ensure you have Python 3 installed on your system.
*   **VirusTotal API Key:** You need a valid VirusTotal API key. You can obtain one by creating a free account on the VirusTotal website.
*   **Python Packages:** Install the required Python packages using pip:

    ```bash
    pip install vt python-dotenv pandas jinja2
    ```

## Installation

1.  **Clone the repository (or download the files):**
    ```bash
    git clone <repository_url> # Replace <repository_url> with the actual URL if you have a repo
    cd VTScan
    ```
2.  **Create a `.env` file:**
    *   In the `VTScan` directory, create a file named `.env`.
    *   Add your VirusTotal API key to this file:

        ```
        VT_API_KEY=your_actual_api_key
        ```
        Replace `your_actual_api_key` with your actual VirusTotal API key.

        Do not share your VirusTotal API key!

## Usage

1.  **Modify `main.py` (for now):**
    *   Open the `main.py` file.
    *   Modify the `urls` list to include the URLs you want to scan:

        ```python
        urls = [
            "example.com",
            "malware.com",
            "another-url.net",
            # Add more URLs here
        ]
        ```

2.  **Run the script:**
    ```bash
    python main.py
    ```

3.  **View the reports:**
    *   After the script finishes, you will find two report files in the `VTScan` directory:
        *   `results.xlsx`: An Excel file containing the scan results.
        *   `report.html`: An HTML file with a formatted report.