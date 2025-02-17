# dew_point

### Goal
Calculate and visualize dew point termperature (T<sub>d</sub>) ([1](#1))  and dew point margin across a wide range of relative humidity and temperature (RH &amp; T) values with a consideration for preventing high humidity and surface condensation in small rooms, e.g. 3 m<sup>3</sup>. 
#

#### LLM Prompt
Calculate dew point from relative humidity and temperature using the magnus formula.
#

#### Explanation & Equation Selection
If RH > 50 % then the dew point temperature (T<sub>d</sub>) in °C can be caluclated fairly accurately using ([2](#2))

T<sub>d</sub> = T - ((100 - RH) / 5)  

<br>
We want to use a more robust calculation to produce correct results across a broad range of RH & T.  
<pre>
RH  %   >  0 → 100
T  °C   - 45 →  60
T  °F   - 49 → 140
</pre>

<br>

Consider a simplified form of the August-Roche-Magnus equation:  
$$T_d = \frac{B \cdot \alpha(T, RH)}{A - \alpha(T, RH)}$$

where  
$$\alpha = \frac{A \cdot T}{B + T} + \ln\left(\frac{RH}{100}\right) $$
<pre>
A    [17.27 →  17.625] = 17.625    dimensionless
B    [237.04 → 243.12] = 243.04    °C
</pre>

https://www.omnicalculator.com/physics/dew-point  

https://journals.ametsoc.org/downloadpdf/view/journals/bams/86/2/bams-86-2-225.pdf


"For the range -45 °C to +60 °C, values given by this equation have an uncertainty of < ±0.6 % of value, at the 95% confidence level." https://www.npl.co.uk/resources/q-a/dew-point-and-relative-humidity  

Adjusting the coefficients can reduce uncertainty for specific, narrower temperature ranges.
The coefficients should also be changed depending on whether the air mass is over water or ice.



 

<br>

### References
#### [1]  https://en.wikipedia.org/wiki/Dew_point
<br>

#### [2] https://iridl.ldeo.columbia.edu/dochelp/QA/Basic/dewpoint.html
Bell, Michael

Lawrence, Mark G., 2005  
The relationship between relative humidity and the dewpoint temperature in moist air: A simple conversion and applications  
Bulletin of the American Meteorlogical Society, Vol. 86, Issue 2, pages 225 - 234  
http://dx.doi.org/10.1175/BAMS-86-2-225

<br>

#### [3]  
https://en.wikipedia.org/wiki/Enthalpy_of_vaporization


<br>

ΔH<sub>vap</sub>  
&emsp; • enthalpy of vaporization  
&emsp; • latent heat of vaporization of water  
&emsp; • heat of evaporation: the amount of energy (enthalpy) that must be added to a liquid  
&emsp; substance to transform a quantity of that substance into a gas. ([3](#3))

https://extensionpubs.unl.edu/publication/g1849/2008/pdf/view/g1849-2008.pdf

https://en.wikipedia.org/wiki/Vapour_pressure_of_water#Accuracy_of_different_formulations  
could use the slightly more complex Buck equation for greater accuraccy

ttp://mc-computing.com/science_facts/Water_Vapor/Other_Formulas.html  
comparison of many papers and the differences in them