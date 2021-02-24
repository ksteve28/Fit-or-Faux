Fit or Faux: A look into Colorado’s Health Data

Background & Motivation

Health has been a growing passion of mine. Living in Colorado there is an abundance of indoor and outdoor activities to partake in and get you moving. Many social interactions even take place around some form of activity or movement. An article written in 2020, published on Exercise.com - “These are the 10 fittest states in America” dubbed Colorado number one. However, with numerous health epidemics on the rise, including obesity I want to know how healthy is the state truly? Is Colorado performing up to the standard to combat these epidemics or could there be room for improvement? By creating additional awareness to these epidemics hopefully it will encourage individuals to make better decisions that will impact their health positively. 

Data
Colorado Department of Public Health & Environment released Community Level Estimates for 18 data sets specific to health conditions and risk behaviors. Some data sets are include Overweight, Obese, Diabetes, Binge Drinking, Asthma, etc. Individual survey responses from the Colorado BRFSS are nested within geographic boundaries (counties) where both individual characteristics (demographic) as well as sociodemographic characteristics can be used to model the the probability of having a condition or risk behavior. 


Exploratory Data Analysis
From the 18 of the data sets I decided to look at the following: Diabetes, Obesity, and Overweight. The CDPHE isolated 64 counties into roughly 1,240 rows with 16 standard columns. Each row is unique with its own Census Tract data. This data provides insight on the County name, adult population over 18 (within that census tract data), health condition or risk behavior estimate, estimate confidence interval, quintile, health condition or risk behavior county regional estimate, and state estimate. 


Although the data was fairly clean there were 18 null values within Overweight and Diabetes and 36 null values for Obesity. CDPHE stated for counties less than 50 people residing data would not be available which may be attribute to the missing data.
Upon cleaning the missing data values I wanted to get a feel for the data. Therefore, I wanted to inspect what the average data population sizes for the selected data sets. 

<img src='images/adults.png'>
<inset violin graphs>


The data appears to be mostly consistent within it's sample size for county groupings.
The median data for Adults over 18 was 3,221+/- and the mean data for Adults over 18 was 3,350+/-. Which made curious as to groupings per county.

<groupings per county>

Further into exploratory analysis let's take a look at some data specific samples of the regions within counties most and least at risk for the health conditions.

<insert lowest and highest census bar plots>

As one can tell there is can be quite a discrepancy so it would be benficial to see where these lay on a total distribution.
<histogram>
<img src="images/overweight_hist.png">
<img src="images/obesity_hist.png">
<img src='images/Diabetes_hist.png'>


Breaking down the data and what does it mean?
Running statiscal and mathmatical approaches to transfer a percentage to total person amount of data. 

Overall, why is this data important and what light does it shed?


Obesity is an epidemic that is entirely taxing on the economy as a whole. Through analysis and estimation through the BFSS surveys we could isolate and target specific counties that are more at risk and implement funding for not only better education, but resources to make better decisions. 
As we have seen with covid, comorbidities were a huge factor that play into health. While this data does not explicity show us there is a direct correlation with obesity and health conditions. 

Through the exploration of this data a question arose in my mind. Would it be more appropriate The state estimates is an overall projection where as the county and regional took into consideration the BRFF surveys and was able to predict. Would it be more useful for the public to have more targeted health anaylsis in order to have more community outrach/etc?

