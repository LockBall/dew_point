import numpy as np
import csv

def dew_point_magnus(T, RH):
    """Calculates dew point using the Magnus formula."""
    T = np.asarray(T)
    RH = np.asarray(RH)

    if np.any(T < -50) or np.any(T > 60) or np.any(RH < 0) or np.any(RH > 100):
        return np.nan

    RH_zero = (RH == 0)
    Td = np.full_like(T, np.nan, dtype=float)

    non_zero_RH = (RH != 0)
    if np.any(non_zero_RH):
        a = 17.27
        b = 237.7
        T_nz = T[non_zero_RH]
        RH_nz = RH[non_zero_RH]
        gamma = (a * T_nz) / (b + T_nz) + np.log(RH_nz / 100)
        Td_nz = (b * gamma) / (a - gamma)
        Td[non_zero_RH] = Td_nz

    Td[RH_zero] = T[RH_zero]
    return Td

def generate_dew_point_table(temp_range, rh_range):
    """Generates a dew point table."""
    table = {}
    for temp in temp_range:
        row = {}
        for rh in rh_range:
            dew_point_val = dew_point_magnus(temp, rh)
            if not np.isnan(dew_point_val):
                row[rh] = f"{dew_point_val:.2f}"
            else:
                row[rh] = "N/A"
        table[temp] = row
    return table

def print_dew_point_table(table):
    """Prints the dew point table in a readable format."""
    rh_range = sorted(list(table[list(table.keys())[0]].keys()))
    print("Temperature (°C) | " + " | ".join(map(str, rh_range)) + " |")
    print("-" * (20 + len(rh_range) * 8))

    for temp, row in sorted(table.items()):
        formatted_row = [row[rh] for rh in rh_range]
        print(f"{temp:16.2f} | " + " | ".join(formatted_row) + " |")

def save_dew_point_table_to_csv(table, filename="dew_point_table_gemini.csv"):
    """Saves the dew point table to a CSV file."""
    rh_range = sorted(list(table[list(table.keys())[0]].keys()))
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        header = ["Temperature (°C)"] + list(map(str, rh_range))
        writer.writerow(header)
        for temp, row in sorted(table.items()):
            formatted_row = [row[rh] for rh in rh_range]
            writer.writerow([f"{temp:.2f}"] + formatted_row)

# Generate and print the table
temp_range = range(-40, 51, 5)
rh_range = range(10, 101, 10)

dew_point_table = generate_dew_point_table(temp_range, rh_range)
print_dew_point_table(dew_point_table)

# Save the table to a CSV file
save_dew_point_table_to_csv(dew_point_table)
print("\nDew point table saved to dew_point_table_gemini.csv")