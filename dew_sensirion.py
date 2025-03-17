from math import log10
from math import log

RH = 50
TC = 40

print('sensirion')
coef_a = 17.62  # dimensionless
coef_b = 243.12  # °C

H = (log10(RH) -2 ) / 0.4343 + (coef_a * TC) / (coef_b + TC)
Dp = coef_b * H / (coef_a - H )
print('Dp', Dp)