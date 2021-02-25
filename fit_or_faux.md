<H1> Fit or Faux: A look into Colorado’s Health Data</H1>

<img src='images/IMG_9740.jpeg'>

# Background & Motivation

Health has been a growing passion of mine. Living in Colorado there is an abundance of indoor and outdoor activities to partake in and get you moving. Many social interactions even take place around some form of activity or movement. An article written in 2020, published on Exercise.com - “These are the 10 fittest states in America” dubbed Colorado number one. However, with numerous health epidemics on the rise, including obesity I want to know how healthy is the state truly? Is Colorado performing up to the standard to combat these epidemics or could there be room for improvement? By creating additional awareness to these epidemics hopefully it will encourage individuals to make better decisions that will impact their health positively. 

# Data
Colorado Department of Public Health & Environment released Community Level Estimates for 18 data sets specific to health conditions and risk behaviors. Some data sets are include Overweight, Obese, Diabetes, Binge Drinking, Asthma, etc. Individual survey responses from the Colorado BRFSS are nested within geographic boundaries (counties) where both individual characteristics (demographic) as well as sociodemographic characteristics can be used to model the the probability of having a condition or risk behavior. 


# Exploratory Data Analysis
From the 18 data sets provided I decided to look at the following: Diabetes, Obesity, and Overweight. The CDPHE isolated 64 counties into roughly 1,240 rows with 16 standard columns. Each row is unique with its own Census Tract data. This data provides insight on the County name, adult population over 18 (within that census tract data), health condition or risk behavior estimate, estimate confidence interval, quintile, health condition or risk behavior county regional estimate, and state estimate. 


Although the data was fairly clean there were 18 null values within Overweight and Diabetes and 36 null values for Obesity. CDPHE stated for counties less than 50 people residing data would not be available which may be attribute to the missing data. In order to reduce graphing errors I also created an additional column to distibguish the census tract id and country name.


Upon cleaning the missing data values I wanted to get a feel for the data. First, I wanted to inspect our sample sizes for the cenesus tracts. How I did this was looking at the column "Adult Population Over 18". As you can tell below, our sample sizes are very consistent among the data sets. This makes sense because the census tracts are based on surveys presented in the same geographical specific region. 

<div align="center">
<img src='images/adults.png' height='300'>
</div>
<br>


The median data for Adults over 18 was roughly 3,221. and the mean data for Adults over 18 was roughly 3,350. Which made curious as to groupings per county.

<groupings per county>

Further into exploratory analysis let's take a look at some data specific samples of the regions within counties most and least at risk for the health conditions.

The following graphs are census and counties with the lowest prevalence rates.



<br>
<div align="center">
<img src="images/lowest_overweight_est.png" height='300'> 
<br>

<img src="images/lowest_obesity_est.png" height='300'> 

<br>

<img src='images/lowest_diabetes_est.png' height='300'>
</div>
<br>

<br>
<div align="center">
<img src="images/highest_overweight_est.png" height='300'> 
<br>

<img src="images/highest_obesity_est.png" height='300'> 

<br>

<img src='images/highest_diabetes_est.png' height='300'>
</div>
<br>

As one can tell there is can be quite a discrepancy so it would be benficial to see where these lay on a total distribution.

<div align="center">
<img src="images/overweight_hist.png" height='400'>

<img src="images/obesity_hist.png" height='400'>

<img src='images/Diabetes_hist.png' height='400'>
</div>
<br>



Breaking down the data and what does it mean?
Running statiscal and mathmatical approaches to transfer a percentage to total person amount of data. 



Findings
Through examing the data further I discovered that out of xxx census county tract estimates 638 exceeded the state estimate and 591 were below for obesity.

Overweight - 535 below state estimations, 

Prior to combining the counties and taking an average 

Grouping the Counties together and divding by their occurance within the census track it is seen that 

Obesity - mean 22.85, median 23.10


| County_Name   |   Obese_Census_Tract_Estimate |
|:--------------|------------------------------:|
| Mineral       |                           2.5 |
| Hinsdale      |                           4.8 |
| San Miguel    |                           5.3 |
| Gunnison      |                           7.7 |
| Pitkin        |                           9.3 |
| Summit        |                          10.8 |


| County_Name   |   Obese_Census_Tract_Estimate |
|:--------------|------------------------------:|
| Costilla      |                         43.7  |
| Jackson       |                         40.2  |
| Bent          |                         39.5  |
| Kit Carson    |                         38.5  |
| Las Animas    |                         36.55 |
| Cheyenne      |                         35.6  |

| County_Name   |   OverweightObese_Census_Tract_Estimate |
|:--------------|----------------------------------------:|
| Hinsdale      |                                 30.90   |
| San Miguel    |                                 31.73   |
| Pitkin        |                                 36.75   |
| Mineral       |                                 36.90   |
| Ouray         |                                 41.4    |
| Eagle         |                                 41.87   |

| County_Name   |   OverweightObese_Census_Tract_Estimate |
|:--------------|----------------------------------------:|
| Bent          |                                  80     |
| Morgan        |                                  74.825 |
| Huerfano      |                                  72.65  |
| Kiowa         |                                  72.4   |
| Prowers       |                                  71.74  |
| Costilla      |                                  70.45  |

Overall, why is this data important and what light does it shed?

Obesity is an epidemic that is entirely taxing on the economy as a whole. Through analysis and estimation through the BFSS surveys we could isolate and target specific counties that are more at risk and implement funding for not only better education, but resources to make better decisions. 
As we have seen with covid, comorbidities were a huge factor that play into health. While this data does not explicity show us there is a direct correlation with obesity and health conditions. 

Through the exploration of this data a question arose in my mind. Would it be more appropriate The state estimates is an overall projection where as the county and regional took into consideration the BRFF surveys and was able to predict. Would it be more useful for the public to have more targeted health anaylsis in order to have more community outrach/etc?

