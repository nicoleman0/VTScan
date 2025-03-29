# VTScan - a VirusTotal URL Scanner

VTScan - an simple FOSS Python-based command-line tool designed to scan URLs using the VirusTotal API, collect scan results, and generate both Excel and HTML reports. Its purpose is to streamline the process of checking multiple URLs for potential threats.

## Prerequisites

*   **Python 3.x:** Ensure you have Python 3 installed on your system.
*   **VirusTotal API Key:** You need a valid VirusTotal API key. You can obtain one by creating a free account on the VirusTotal website.
*   **Python Packages:** Install the required Python packages using pip:

    ```bash
    pip install vt python-dotenv pandas jinja2
    ```

## Installation

*  **Clone the repository (or download the files):**
    ```bash
    git clone https://github.com/nicoleman0/VTScan 
    cd VTScan
    ```

## How to Use

*  **Run the script:**
    ```bash
    python3 main.py
    ```

*  **View the reports:**
    *   After the script finishes, you will find two report files in the `VTScan` directory:
        *   `results.xlsx`: An Excel file containing the scan results.
        *   `report.html`: An HTML file with a formatted report.

## Commands

*   **URL Scanning**
    *   To scan for URLs:   
        
        ```bash
        python3 main.py example.com malware.com another-url.net
        ```
    *   For help:
        ```bash
            python3 main.py --help
            python3 main.py -h
        ```