# 🛡️ VTScan: VirusTotal URL Scanner

VTScan is a command-line tool for scanning URLs using the VirusTotal API and generating reports.

## ✨ Features

- 🕵️ Scan multiple URLs against VirusTotal.
- 🔑 Provide your API key as an option or when prompted.
- 📊 Generate results as an Excel file (`results.xlsx`) and an HTML report (`report.html`).
- 🟢 Clear progress updates and error handling.

## 🛠 Prerequisites

- 🐍 Python 3.7+
- 🛡️ VirusTotal API Key (available for free from VirusTotal)
- 📦 Python packages: `typer`, `typing_extensions`, `vt`, `pandas`, `jinja2`

## 🚀 Installation

1. Clone the repository or download the files.
2. Navigate to the project directory.
3. Install the required dependencies:

    ```bash
    pip install typer typing_extensions vt pandas jinja2
    ```

## 🧑‍💻 Usage

Run the tool using the following command:

```bash
python main.py <url1> <url2> ... [options]
```

To see the available options, run:

```bash
python main.py --help
```

## 📜 License

This project is licensed under the MIT License. See the LICENSE file for details.

