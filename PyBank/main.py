
import os
import csv
from pathlib import Path 

# Locate data
input = Path("Resources", "budget_data.csv")

# Where will be located the data
totalbymonths = []
allprofit = []
variationbymonth = []
 # Open csv file
with open(input,newline="", encoding="utf-8") as forecast:

    csvreader = csv.reader(forecast,delimiter=",") 
   
    header = next(csvreader)  

    # Look up each rows in the data
    for row in csvreader: 
      # Add total profit
        totalbymonths.append(row[0])
        allprofit.append(int(row[1]))

    # Goes for all to get the monthly changes
    for i in range(len(allprofit)-1):
        
        variationbymonth.append(allprofit[i+1]-allprofit[i])
        
# Identify the maximum of increase and minimum 
maximumincrease = max(variationbymonth)
minimumdecrease = min(variationbymonth)

# Identify the maximum of increase and minimum by month
maximumincreasemonth = variationbymonth.index(max(variationbymonth)) + 1
maximumdecreasemonth = variationbymonth.index(min(variationbymonth)) + 1 

# Final results

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {len(totalbymonths)}")
print(f"Total: ${sum(allprofit)}")
print(f"Average Change: {round(sum(variationbymonth)/len(variationbymonth),2)}")
print(f"Greatest Increase in Profits: {totalbymonths[maximumincreasemonth]} (${(str(maximumincrease))})")
print(f"Greatest Decrease in Profits: {totalbymonths[maximumdecreasemonth]} (${(str(minimumdecrease))})")

