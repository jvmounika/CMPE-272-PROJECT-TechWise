The link for the assignment USGS site provides the downloadable CSV files having data of Earthquakes happened in the past 5min or 1 day or 1 week or 1 month or years.
Tasks done in this project:

Downloading the csv file from USGS website to give details on past 7    days Earthquake worldwide.

1) Reading the csv file(earthquake magnitude >2.5) and storing its data:
    
	data= pd.read_csv("2.5_day.csv")

2) Finding all the places with the Earthquake magnitude >3
	
	newt = data[["place", "mag", "time"]]
	newt2=newt[(newt.mag >= 3)]

3) Statistical analysis of earthquake magnitude to give average            magnitude, total count of number of times earthquake happened and
   percentiles. 
	
	data.describe()
4) Displaying all the affeacted areas name only once.

	places= pd.DataFrame(data["place"].unique(), columns=["All         Affected areas"])
	places

5) Number of times each Earthquake magnitude occured.

	newdata = data["mag"].value_counts()


Future work:

1)This statictical analysis on past earthquake events of several years can be used to develop algorithm to predict earthquakes.

2)Mining the new model referred to as the third Uniform California Earthquake Rupture Forecast, or “UCERF3” is the future for Earthquake prediction.