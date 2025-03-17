# dew_point

### Goal
Calculate and visualize dew point termperature (T<sub>d</sub>) ([1](#1))  and dew point margin across a wide range of relative humidity and temperature (RH &amp; T) values with a consideration for preventing high humidity and condensation in small rooms, e.g. 3 m<sup>3</sup>. 
#

#### Explanation & Equation Selection
If RH > 50 % then the dew point temperature (T<sub>d</sub>) in °C can be caluclated fairly accurately using ([2](#2))

<!--  T<sub>d</sub> = T - ((100 - RH) / 5)  -->
$$T_d = T - \left(\frac{100 - RH}{5}\right)$$


<br>
We want to use a more robust calculation to produce correct results across a broader range of RH & T.  
<pre>
RH  %   >  0  →  + 100
T  °C   - 45  →  +  60
T  °F   - 49  →  + 140
</pre>

<br>

Consider a simplified form of the August-Roche-Magnus equation ([5](#5)):  
$$T_d = \frac{B \cdot \alpha(T, RH)}{A - \alpha(T, RH)}$$

where  
$$\alpha = \frac{A \cdot T}{B + T} + \ln\left(\frac{RH}{100}\right) $$
and the coefficients A and B are  
<pre>
 17.27 < A <  17.625  =  17.625    dimensionless
237.04 < B < 243.12   =  243.04    °C
</pre>

The python code to calculate this is  
<pre>
coef_a = 17.625  # dimensionless
coef_b = 243.04  # °C

alpha = (coef_a * TC) / (coef_b + TC) + log(RH / 100)  # natural log ln
Td = (coef_b * alpha) / (coef_a - alpha)
</pre>
#

Sensirion, a company that specializes in sensors uses a similar approach and provides  sample code ([4](#4))  

there are additional details in


<pre>
h = (log10(RH)-2.0) / 0.4343 + (17.62 * T) / (243.12 + T);
Td = 243.12*h/(17.62-h);
</pre>

We can see that they are using similar coefficients as the previous example.  
Note that the value *0.4343* is an approximation of 1 / ln(10) which is a conversion of base 10 log to natural log.

If we compare the output of the two from 0 < RH < 100 and -40 < TC < 60 we can determine that the differences between the two methods in °C are min 0.00, max 0.03 and avg 0.01

If we adjust the sensirion code to use the same coefficients and natural log then we see that the differences in output between the two approaches is zero out to at least 8 decimal places

#



https://journals.ametsoc.org/downloadpdf/view/journals/bams/86/2/bams-86-2-225.pdf


"For the range -45 °C to +60 °C, values given by this equation have an uncertainty of < ±0.6 % of value, at the 95% confidence level." https://www.npl.co.uk/resources/q-a/dew-point-and-relative-humidity  

Adjusting the coefficients can reduce uncertainty for specific, narrower temperature ranges.

#

### References
#### [1]  https://en.wikipedia.org/wiki/Dew_point


#### [2] https://iridl.ldeo.columbia.edu/dochelp/QA/Basic/dewpoint.html
Bell, Michael

#

coefficients et al  
Lawrence, Mark G., 2005  
The relationship between relative humidity and the dewpoint temperature in moist air: A simple conversion and applications  
Bulletin of the American Meteorlogical Society, Vol. 86, Issue 2, pages 225 - 234  
http://dx.doi.org/10.1175/BAMS-86-2-225
https://journals.ametsoc.org/downloadpdf/view/journals/bams/86/2/bams-86-2-225.pdf


#### [3]  https://en.wikipedia.org/wiki/Enthalpy_of_vaporization


#### [4]  https://sensirion.com/media/documents/A419127A/6163F5FE/Sensirion_AppNotes_Humidity_Sensors_at_a_Glance.pdf  


#### [5]
https://www.omnicalculator.com/physics/dew-point  

####[6]
https://irtfweb.ifa.hawaii.edu/~tcs3/tcs3/Misc/Dewpoint_Calculation_Humidity_Sensor_E.pdf  plot of deviation of magnus from hardy min max for the entire plot of - 0.35 to 0.5 °C




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

#

### dew point tables & Calculators
an effort to find known values to compare output of code. difficult to find anythign with references  

terrible https://www.nwcg.gov/publications/pms437/weather/temp-rh-and-dew-point-tables?form=MG0AV3  

https://xlbrands.com/wp-content/uploads/2021/09/TechnicalBulletin-SUBSTRATE_DewPointCalculationChartenglish-053118.pdf converted from F to C Bostik commercial floor covering
4 < TC < 33    30 < RH < 90  

https://lamtec.com/technical-bulletins/dew-point-table/?form=MG0AV3  
insulation vapor retarders and building facings  
0 < TC < 43    10 < RH < 100  

https://bmcnoldy.earth.miami.edu/Humidity.html  

https://www.tis-gdv.de/tis_e/misc/klima-htm/  
German Insurance Assoc. Transport Information Service
-25 < TC < 50    10 < RH < 100  

https://www.korff.ch/wp-content/uploads/2021/01/Taupunkt-Tabelle-EN.pdf  
specialty aluminum foil vapour barrier  
2 < TC < 50    45 < RH < 95

https://www.dur-a-flex.com/wp-content/uploads/2020/02/dew-point-calculation-chart.pdf  
seamless flooring
-70 < TC < 50    30 < RH < 90

https://www.prokol.com/wp-content/uploads/2021_Dew-point-table.pdf  
protective coatings
2 < TC < 50    45 < RH < 95  

<pre>
mins and maxes from whole # tables include Min and max of data in all tables  
Temp (C) - 25  →  + 50  
RH (%)     10  →   100  
</pre>

tables from Lamtec, KORFF, Prokol, and TIS have whole number input  
tables from Dur_a_flex and XL brands have decimal input ∵ they were converted from F to C