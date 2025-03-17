import numpy as np
import matplotlib.pyplot as plt
from math import log10, log

# Declare variables for storing data and coefficients
rh_values = []
differences = []
tc_values = []

coef_a_sens = 17.625  # 17.62
coef_b_sens = 243.04  # 243.12

coef_a_arm = 17.625
coef_b_arm = 243.04

# Start and increment values for TC and RH_percent
TC_start = -45.00  # Starting temperature (°C)
TC_end = 60.00     # Ending temperature (°C)
TC_increment = 1.00  # Increment for temperature (°C)

RH_start = 0.00    # Starting relative humidity (%)
RH_end = 100.00    # Ending relative humidity (%)
RH_increment = 1.00  # Increment for relative humidity (%)

print_enable = 1
plot_enable = 0

with open("dew_ARM_sens_compare.csv", "w") as csvfile:
    csvfile.write("T (C), RH (%), Dp_sens, Td_ARM, Difference Abs\n")

    TC = TC_start  # Initialize temperature
    while TC <= TC_end:  # Loop over temperatures
        RH_percent = RH_start  # Initialize relative humidity
        while RH_percent <= RH_end:  # Loop over relative humidity
            RH_decimal = RH_percent / 100.0  # Convert RH to decimal for ARM calculation

            rh_values.append(RH_percent)  # Store percent values for plots
            tc_values.append(TC)

            if RH_percent > 0.00:
                H = (log10(RH_percent) - 2) / (1/log(10)) + (coef_a_sens * TC) / (coef_b_sens + TC)
                Dp_sens = coef_b_sens * H / (coef_a_sens - H)
                # 1/log(10) = 0.4343  log is ln

                alpha_arm = (coef_a_arm * TC) / (coef_b_arm + TC) + log(RH_decimal)  # Use decimal value
                Td_ARM = coef_b_arm * alpha_arm / (coef_a_arm - alpha_arm)
            else:
                Dp_sens = TC
                Td_ARM = TC

            dec_place = 8
            difference = abs(Dp_sens - Td_ARM)  # Absolute value of the difference
            csvfile.write(
                            f"{TC:.{dec_place}f},"
                            f"{RH_percent:.{dec_place}f},"
                            f"{Dp_sens:.{dec_place}f},"
                            f"{Td_ARM:.{dec_place}f},"
                            f"{difference:.{dec_place}f}\n"
                        )

            differences.append(difference)

            RH_percent += RH_increment  # Increment RH

        TC += TC_increment  # Increment temperature

# Calculate min and max differences
min_diff = min(differences)
max_diff = max(differences)
avg_diff = sum(differences) / len(differences)  # average


if print_enable == 1:
    print(f"Minimum Difference: {min_diff:.2f}°C")
    print(f"Max Difference: {max_diff:.2f}°C")
    print(f"Avg Difference: {avg_diff:.2f}°C")

# terminal prompt remains open until figure is closed
if plot_enable == 1:
    # Create the difference plot
    plt.figure(figsize=(12, 6))
    scatter = plt.scatter(tc_values, differences, c=rh_values, cmap='viridis', s=10)  # Use scatter, color by RH
    cbar = plt.colorbar(scatter, label='Relative Humidity (%)')
    
    # Flip the colorbar
    cbar.ax.invert_yaxis()  # 100 at the bottom and 0 at the top

    # Add min and max lines for differences
    plt.axhline(y=min_diff, color='blue', linestyle='--', label=f"Min Difference: {min_diff:.2f}°C")
    plt.axhline(y=max_diff, color='red', linestyle='--', label=f"Max Difference: {max_diff:.2f}°C")
   
    # Plot the Plot
    plt.xlabel("Temperature (°C)")
    plt.ylabel("Absolute Difference (°C)")
    plt.title("Absolute Difference Between Sensirion and ARM Dew Point Calculations")
    plt.grid(True)
    plt.legend()

    plt.show()