"""
created by: Lutz, John P.
created date: 13 feb 2025
license: MIT

Calculate and return the dew point temperature (Td °C)
given relative humidity (RH %) and temperature (TC °C)
using the August-Roche-Magnus formula

https://www.omnicalculator.com/physics/dew-point

   0 < RH ≤ 100
- 45 < TC <  60 
"""

from math import log

def calc_Td(RH, TC):

    coef_a = 17.625  # dimensionless
    coef_b = 243.04  # °C

    alpha = (coef_a * TC) / (coef_b + TC) + log(RH / 100)  # natural log ln
    Td = (coef_b * alpha) / (coef_a - alpha)
    return Td


start_RH = 0
end_RH = 5
inc_RH = 1

for RH in range(start_RH, end_RH + 1, inc_RH):
    if RH != 0 :
        TC = 25  # Celsius
        Td = calc_Td(RH, TC)
        print(f"RH: {RH:.2f} %    "  , f"Dew point: {Td:.3f} °C")
    else :
        print('undefined RH') 

    