from openpyxl import Workbook


def save_to_excel(results, file_name="results.xlsx"):
    wb = Workbook()
    ws = wb.active
    ws.append(["URL", "Malicious Engines",
              "Harmless Engines", "Undetected Engines"])

    for result in results:
        ws.append([
            result.get('url', 'N/A'),
            result.get('malicious', 0),
            result.get('harmless', 0),
            result.get('undetected', 0)
        ])

    wb.save(file_name)
    print(f"Results saved to {file_name}")
