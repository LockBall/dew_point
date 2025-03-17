import numpy as np
import pandas as pd

# Define the August-Roche-Magnus equation
def calculate_dew_point(temp, rh):
    a, b = 17.625, 243.04  # Constants for the equation
    alpha = (a * temp) / (b + temp) + np.log(rh / 100.0)
    dew_point = (b * alpha) / (a - alpha)
    return round(dew_point, 2)  # Round to 2 decimal places

# Generate a range of temperatures and relative humidity values
temperatures = np.arange(-40, 51, 5)  # From -40°C to 50°C (inclusive) in 5°C steps
relative_humidities = np.arange(10, 101, 10)  # From 10% to 100% in 10% steps

# Create a table of dew points
data = []
for temp in temperatures:
    row = [calculate_dew_point(temp, rh) for rh in relative_humidities]
    data.append(row)

# Convert to a DataFrame for better visualization
columns = [f"{rh}%" for rh in relative_humidities]
df = pd.DataFrame(data, index=temperatures, columns=columns)
df.index.name = "Temperature (°C)"
df.columns.name = "Relative Humidity"

# Save to a CSV file
df.to_csv("dew_point_table.csv")
print("Dew point table saved as 'dew_point_table.csv'")
