# dew_point
Calculate and visualize dew point ([1](#1))  and dew point margin across a wide range of relative humidity and temperature (RH &amp; T) with a consideration for preventing high humidity and surface condensation in small rooms, e.g. 3 m<sup>3</sup>. 


if RH > 50 % then the dew point temperature (T<sub>d</sub>) in °C can be caluclated fairly accurately using ([2](#2))

T<sub>d</sub> = T - ((100 - RH) / 5)  

<br>
We want to use a more robust calculation, i.e. something that can produce correct results across a broad range of RH & T.  
<pre>
RH  %  :     0 → 100   
T  °C  :  -135 → 135
</pre>
<br>

August-Roche-Magnus  
constants  

ΔH<sub>vap</sub>  :&emsp; 17.27 → 17.62  
&emsp; • enthalpy of vaporization  
&emsp; • latent heat of vaporization of water  
&emsp; • heat of evaporation: the amount of energy (enthalpy) that must be added to a liquid  
&emsp; substance to transform a quantity of that substance into a gas. ([3](#3))

average temperature in the range of interest 237.7

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


https://extensionpubs.unl.edu/publication/g1849/2008/pdf/view/g1849-2008.pdf
