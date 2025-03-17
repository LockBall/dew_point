"""
author: Lutz, John P.
create date: 13 feb 2025
change date: 27 feb 2025
license: MIT

given relative humidity (RH %) and temperature in °C (TC)
use the August-Roche-Magnus formula to Calculate the dew point temperature (Td) in °C

https://www.omnicalculator.com/physics/dew-point

       0 < RH ≤ 100
    - 45 < TC <  60 

assume analog sensors and an arbitrary calculation interval with no data caching prior to request
    5 < Hz < 0.2
∴ batch data cannot be input to the function ∵ it is not known yet

for the simple formula, known values from Equation 1
https://journals.ametsoc.org/downloadpdf/view/journals/bams/86/2/bams-86-2-225.pdf

15 °C
50 <= RH % <= 100  : increment = 5 %
Td = 5 → 15 : increment = 1
11 discreet data points
"""
# generate the data and store it in memory !!
# input, input, result check
# no need to generate the entire thing. generate a single iteration of necessary, do the thing, save the result


from math import log
import time

print('dew point calculations & comparisons')


'''
# Prompt the user for input
user_input = input("Enter something: ")

# Print the user's input
print("You entered:", user_input)
'''

#  the simple calculation input paramters are the limiting factor in the comparison
#  initial timing comparisons performed using simple ranges as inputs

# a test is limited by known valid data to compare output to
# ∴ expected data drives the test

verbose = False
TC = 15  # Celsius

# RH_in TC_in Td_exp 

RH_range_simp = [50, 100, 5]  #  begin, cease, increment
#  50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100
Td_expect_simp = list(range(5, 16, 1))  # verified output as shown below
# start: inclusive 5, end: 15 exclusive 16, increment 1
# expected Td output as RH increases from 50 → 100 inclusive in increments of 5 @ TC = 15 °C
# [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

num_elements = len(my_list)


#  50 <  RH <= 100
#   0 <= TC <=  30
def calc_Td_simp(RH, TC):
    Td = TC - ((100 - RH) / 5)
    return Td


#    0 <  RH <= 100
# Rh > 0 ∵ log, ln (0) = undef
#  -45 <= TC <= 140
def calc_Td_ARM(RH, TC):

    coef_a = 17.625  # dimensionless
    coef_b = 243.04  # °C

    log_term = log(RH / 100)
    print(log_term)

    alpha = (coef_a * TC) / (coef_b + TC) + log(RH / 100)  # natural log ln
    Td = (coef_b * alpha) / (coef_a - alpha)
    return Td


def measure_loop_time(func, gold_data):
    start_time = time.process_time()
    for data in gold_data:


    # measure the time to do a function based on params
    end_time = time.process_time()
    elapsed_time = end_time - start_time
    return elapsed_time


elapsed_time = measure_loop_time(calc_Td_simp)
print(elapsed_time)

# calc_Td_func_list = [calc_Td_simp, calc_Td_ARM]



# print('iterating ?? with timing')


# time_test = measure_loop_time()

'''
for RH in range(RH_begin, RH_cease + 1, inc_RH):
    if RH != 0 :
        Td = calc_Td_simp(RH, TC)

        #if verbose:
        #    print(f"RH: {RH:.2f} %    "  , f"Dew point: {Td:.3f} °C")

    else :
        #if verbose:
        #    print('undefined RH') 
        Td = None
'''


   