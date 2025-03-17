import pandas as pd

def fahrenheit_to_celsius(f):
    """
    Convert Fahrenheit to Celsius.
    Formula: (°F - 32) * 5/9 = °C
    """
    try:
        if pd.isna(f):  # Skip empty cells (NaN values)
            return None  # Maintain as empty
        return (f - 32) * 5 / 9
    except TypeError:
        return None  # Handle unexpected non-numeric values gracefully

# Load the Excel file
# Replace 'input.xlsx' with the path to your actual Excel file
file_path = 'input.xlsx'
data = pd.read_excel(file_path, engine='openpyxl')

# Ignore the first row and column
data_without_first_row_col = data.iloc[1:, 1:]

# Apply conversion for each value in the table
converted_table = data_without_first_row_col.applymap(fahrenheit_to_celsius)

# Save the converted table to a new Excel file
output_path = 'converted_table.xlsx'
converted_table.to_excel(output_path, index=False, header=False)

print("Converted table saved as 'converted_table.xlsx'.")
