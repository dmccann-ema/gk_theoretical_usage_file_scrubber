from tkinter import filedialog

import pandas as pd

def scrub_excel_file(excel_file_path):
    # Read the Excel file into a pandas DataFrame
    try:
        df = pd.read_excel(excel_file_path)
    except FileNotFoundError:
        print(f"Error: The file '{excel_file_path}' was not found.")
        exit()

    df.columns = df.iloc[3]
    df = df[4:]
    
    first_col = df.iloc[:, 0]
    unit_col = df.iloc[:, 7]
    sold_col = df.iloc[:, 10]
    use_col = df.iloc[:, 15]

    cleaned_df = df[
        first_col.notna() & 
        (first_col != '') & 
        (first_col != df.columns[0]) & 
        unit_col.notna() & 
        sold_col.notna() & 
        use_col.notna()
    ].dropna(axis='columns', how='all')

    file_path_parts = excel_file_path.split('.')

    excel_file_path_scrubbed = '.'.join(file_path_parts[:-1] + ['scrubbed', file_path_parts[-1]])

    cleaned_df.to_excel(excel_file_path_scrubbed, index=False, engine='openpyxl')
    
    return excel_file_path_scrubbed


if __name__ == "__main__":
 
    file_path = filedialog.askopenfilename(
        title = "Select a file",
        filetypes = [("Excel files", "*.xls?"),]
    )

    if file_path:
        scrubbed_file_path = scrub_excel_file(file_path)
        print(f"Excel file '{file_path}' has been scrubbed and saved to '{scrubbed_file_path}'.")

    else:
        print("No file selected. Operation canceled.")