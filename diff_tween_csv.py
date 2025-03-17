import pandas as pd

def compare_matching_csv_files(file1, file2):
    """
    Compares two CSV files with similar formatting to check the differences
    in values for matching temperatures (rows) and relative humidities (columns),
    while ignoring NaN values and displaying only nonzero differences.
    Additionally, counts the number of comparisons made.

    Parameters:
        file1 (str): Path to the first CSV file.
        file2 (str): Path to the second CSV file.

    Returns:
        tuple: A list of nonzero differences and the total number of comparisons.
    """
    # Load the CSV files into DataFrames
    df1 = pd.read_csv(file1, index_col=0)
    df2 = pd.read_csv(file2, index_col=0)

    # Print the loaded files
    print("Contents of File 1:")
    print(df1)
    print("\nContents of File 2:")
    print(df2)
    print()

    # Find common rows (temperatures) and columns (RH levels)
    common_rows = df1.index.intersection(df2.index)
    common_columns = df1.columns.intersection(df2.columns)

    # Filter the DataFrames to only keep matching rows and columns
    df1_filtered = df1.loc[common_rows, common_columns]
    df2_filtered = df2.loc[common_rows, common_columns]

    # Compare the values and record nonzero differences while ignoring NaN
    nonzero_differences = []
    comparison_count = 0  # Initialize comparison count
    for temp in common_rows:  # Iterate over common temperatures (rows)
        for rh in common_columns:  # Iterate over common RH levels (columns)
            value1 = df1_filtered.at[temp, rh]
            value2 = df2_filtered.at[temp, rh]
            if pd.notna(value1) and pd.notna(value2):  # Skip NaN values
                difference = value1 - value2
                comparison_count += 1  # Increment the comparison counter
                if difference != 0:  # Only store nonzero differences
                    nonzero_differences.append((temp, rh, value1, value2, difference))

    return nonzero_differences, comparison_count

# Example usage
file1 = 'lamtec.csv'  # Replace with your first CSV file path
file2 = 'tis.csv'  # Replace with your second CSV file path

nonzero_differences, total_comparisons = compare_matching_csv_files(file1, file2)

if nonzero_differences:
    print("Nonzero Differences (Temp, RH, File1 Value, File2 Value, Difference):")
    for diff in nonzero_differences:
        print(f"Temp: {diff[0]}, RH: {diff[1]}, File1: {diff[2]}, File2: {diff[3]}, Difference: {diff[4]}")
else:
    print("No nonzero differences found.")

print(f"Total number of values compared: {total_comparisons}")
