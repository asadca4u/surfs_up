# surfs_up
### Overview of the analysis:
- The purpose of this analysis was to determine if a surf and shake shop would be a feasible idea on the Hawaiian Islands. 
- Using weather data from various collecting stations, contained in an SQLite database, we determined whether or not the surf and shake shop would be a year round prospect, or merely seasonal.
- Using SQLAlchemy, queries were run in Python to extract data from the SQLlite database.
  - Precipitation data was analyzed and plotted using matplotlib. 
  - Temperature data was also analyzed and plotted. 
- Finally, Flask was used to create a webpage displaying the data so that investors have easy access to insights. 

### Results:
- The temperatures in both June and December remain relatively similar:
  - The average temperature in June is a very nice 74.9F.
  - The average temperature in December is still a very pleasant 71.0F. 
  
- The minimum temperature in December is a fairly cold 56.0F, which seems to be an outlier as more than 75% of the data has temperatures recorded above 69.0F, and 56.0F is more than 3 standard deviations away from the 25th percentile. As a result, we can expect that temperatures below 69.0F will be relatively rare, even in December. 

- The maximum recorded temperatures for both months are also very similar, with 85.0F for June and 83.0F for December respectively. 
  - This indicates that the temperature does not reach any sort of ridiculous highs that may also impede business.
  
  
  
![June_Temps](https://github.com/asadca4u/surfs_up/blob/master/resources/June_Temps.png)![December_Temps](https://github.com/asadca4u/surfs_up/blob/master/resources/December_Temps.png)



### Summary: Provide a high-level summary of the results and two additional queries that you would perform to gather more weather data for June and December.
- Overall, the temperatures seem to stay relatively temperate through the summer and winter, when temperatures are expected to reach their highest and lowest extremes repectively. 
- Since percipitation is also a key indicator of prime surfing and ice cream eating conditions, it would be useful to gather percipiation data for June and December as well. 
- Also, while temperature is expected to stay relatively consistent through the spring and autumn seasons, percipitation generally increases in the spring and autunm, atleast relative to summer. To get a more comprehensive picture of how feasible the shop would be year round, it may be useful to sample precipitation data from March and September as well. 
