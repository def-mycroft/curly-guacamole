

# Dataset Sources

zipcode/population mapping: [FactFinder](https://factfinder.census.gov/faces/tableservices/jsf/pages/productview.xhtml?pid=DEC_10_SF1_GCTP5.ST09&prodType=table)

zipcode/coordinates/cityname mapping: pyzipcode, zipcode Python libraries 

# Notes  

I started working on this in a bootstrap manner, now I want to refine it. 

For some reason, I was missing data from IL, VA, and possibly NE states. 

I found a new dataset from [FactFinder](https://factfinder.census.gov/faces/tableservices/jsf/pages/productview.xhtml?pid=DEC_10_SF1_GCTP5.ST09&prodType=table)

Title of data: 

GCT-P5 Population in Households, Families, and Group Quarters: 2010 - State -- 5-digit ZIP Code Tabulation Area  more information
2010 Census Summary File 1 

I'm going to run this through the same process and see what happens.

After much effort, I was able to find all of the zip codes. I'm confident that I have a full data set now. One hard part was figuring out what zipcode lookup to use, zipcode didn't include all values, geopy got stuck, finally pyzipcode found the ones I was missing. 

I have the data in csv format in google drive, title 'zipcode city population coordinates.zip'

