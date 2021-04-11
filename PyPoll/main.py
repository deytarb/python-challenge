
import os
import csv
from pathlib import Path 

# Where is the path
path = Path("Resources","election_data.csv")

# Assign variables to store data
votesall = 0 
khan = 0
correy = 0
li = 0
otooley = 0

# Bring csv file
with open(path,newline="", encoding="utf-8") as elections:
    csv = csv.reader(elections,delimiter=",") 

    # Look up in the header
    header = next(csv)     

    # Go over over all rows
    for row in csv: 

        votesall +=1

        # How many times each candidate appear
        if row[2] == "Khan": 
            khan +=1
        elif row[2] == "Correy":
            correy +=1
        elif row[2] == "Li": 
            li +=1
        elif row[2] == "O'Tooley":
            otooley +=1

 # create a dictionay inluding  candidates
candidate = ["Khan", "Correy", "Li","O'Tooley"]
No_votes = [khan, correy,li,otooley]

# Getting the winner 
dict_candidates_and_votes = dict(zip(candidate,No_votes))
key = max(dict_candidates_and_votes, key=dict_candidates_and_votes.get)

# Summary
khan_percent = round((khan/votesall) * 100)
correy_percent = round((correy/votesall) * 100)
li_percent = round((li/votesall)* 100)
otooley_percent = round((otooley/votesall) * 100)

# Results
print(f"Election Results")
print(f"----------------------------")
print(f"Total Votes: {votesall}")
print(f"----------------------------")
print(f"Khan: {khan_percent:.3f}% ({khan})")
print(f"Correy: {correy_percent:.3f}% ({correy})")
print(f"Li: {li_percent:.3f}% ({li})")
print(f"O'Tooley: {otooley_percent:.3f}% ({otooley})")
print(f"----------------------------")
print(f"Winner: {key}")
print(f"----------------------------")