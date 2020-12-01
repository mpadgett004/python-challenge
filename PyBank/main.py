# Importing modules needed to find file path
import os, csv
from pathlib import Path

# Setting path through OS to CSV file based on local directories
input_file = Path("Resources","budget_data.csv")

# Creating variables that will represent the info needed. Info will be stored as a list.
total_months = []
total_profit = []
average_change = []

# Opening CSV using the previously created file path variable
with open(input_file) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Moving to the next row in the CSV since the first contains the field names as a header
    header = next(csvreader)

    # For loop that iterates through the rows of the CSV
    for row in csvreader:
        total_months.append(row[0])
        total_profit.append(int(row[1]))

    # Another For loop that iterates through the rows for the monthly profit change
    for i in range(len(total_profit) - 1):
        average_change.append(total_profit[i + 1] - total_profit[i])

# Using the previous created list for the average change, we can find the max and min of the monthly changes
max_increase = max(average_change)
max_decrease = min(average_change)

# Also using the list for average change we can then find and set the max and min needed for the analysis
max_increase_month = average_change.index(max(average_change)) + 1
max_decrease_month = average_change.index(min(average_change)) + 1

# Print the information for the analysis
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {len(total_months)}")
print(f"Total: ${sum(total_profit)}")
print(f"Average Change: {round(sum(average_change) / len(average_change), 2)}")
print(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(max_increase))})")
print(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(max_decrease))})")

# Set file path for text file that will show the analysis
output_file = Path("Analysis","Financial_Analysis_Summary.txt")

with open(output_file, "w") as txtfile:
    # Writing to the text file to show the analysis
    txtfile.write("Financial Analysis")
    txtfile.write("\n")
    txtfile.write("----------------------------")
    txtfile.write("\n")
    txtfile.write(f"Total Months: {len(total_months)}")
    txtfile.write("\n")
    txtfile.write(f"Total: ${sum(total_profit)}")
    txtfile.write("\n")
    txtfile.write(f"Average Change: {round(sum(average_change) / len(average_change), 2)}")
    txtfile.write("\n")
    txtfile.write(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(max_increase))})")
    txtfile.write("\n")
    txtfile.write(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(max_decrease))})")





