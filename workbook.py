import pandas as pd


def save_to_excel(results, file_name="results.xlsx"):
    df = pd.DataFrame(results)
    try:
        df.to_excel(file_name, index=False)
        print(f"Results saved to {file_name}")
    except Exception as e:
        print(f"Error saving the Excel file: {e}")
