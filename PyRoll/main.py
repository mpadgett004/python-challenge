# Importing modules need to go through OS and use CSV file
import os
import csv
from pathlib import Path

# Setting variable for file path based on local directories
csvpath = Path("Resources", "election_data.csv")

# Setting variable to start recording votes values
total_votes = 0
khan_votes = 0
correy_votes = 0
li_votes = 0
otooley_votes = 0

# Opeing CSV file using the already set path variable
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")

    # Skipping first row in CSV because it contains the fields as a header
    header = next(csvreader)

    # For loop to start iterating through each row in the CSV
    for row in csvreader:

        total_votes +=1

        # Using a nest If statement to look at the candidate in each row to then increment their...
        # total if that value is equal to their name
        if row[2] == "Khan":
            khan_votes +=1
        elif row[2] == "Correy":
            correy_votes +=1
        elif row[2] == "Li":
            li_votes +=1
        elif row[2] == "O'Tooley":
            otooley_votes +=1

 # Create two seperate lists to hold the candidate's name and also hold their votes totals
candidates = ["Khan", "Correy", "Li","O'Tooley"]
votes = [khan_votes, correy_votes,li_votes,otooley_votes]

# Taking the two lists and combining them with zip so that a dictionary will now hold the two lists
dict_candidates_and_votes = dict(zip(candidates,votes))
key = max(dict_candidates_and_votes, key=dict_candidates_and_votes.get)

# Turing values into percents for the analysis
khan_percent = (khan_votes/total_votes) *100
correy_percent = (correy_votes/total_votes) * 100
li_percent = (li_votes/total_votes)* 100
otooley_percent = (otooley_votes/total_votes) * 100

# Prints out information based on results
print(f"Election Results")
print(f"----------------------------")
print(f"Total Votes: {total_votes}")
print(f"----------------------------")
print(f"Khan: {khan_percent:.3f}% ({khan_votes})")
print(f"Correy: {correy_percent:.3f}% ({correy_votes})")
print(f"Li: {li_percent:.3f}% ({li_votes})")
print(f"O'Tooley: {otooley_percent:.3f}% ({otooley_votes})")
print(f"----------------------------")
print(f"Winner: {key}")
print(f"----------------------------")

# Setting the path of the text file that will show the analysis
output_file = Path("Analysis", "Election_Results_Summary.txt")

with open(output_file,"w") as txtfile:

# Writes the analysis to the text file
    txtfile.write(f"Election Results")
    txtfile.write("\n")
    txtfile.write(f"----------------------------")
    txtfile.write("\n")
    txtfile.write(f"Total Votes: {total_votes}")
    txtfile.write("\n")
    txtfile.write(f"----------------------------")
    txtfile.write("\n")
    txtfile.write(f"Khan: {khan_percent:.3f}% ({khan_votes})")
    txtfile.write("\n")
    txtfile.write(f"Correy: {correy_percent:.3f}% ({correy_votes})")
    txtfile.write("\n")
    txtfile.write(f"Li: {li_percent:.3f}% ({li_votes})")
    txtfile.write("\n")
    txtfile.write(f"O'Tooley: {otooley_percent:.3f}% ({otooley_votes})")
    txtfile.write("\n")
    txtfile.write(f"----------------------------")
    txtfile.write("\n")
    txtfile.write(f"Winner: {key}")
    txtfile.write("\n")
    txtfile.write(f"----------------------------")