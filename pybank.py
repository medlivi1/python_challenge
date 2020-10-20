# PyBank:  Python script for analyzing the financial records of your company
import os
import csv

input_path = os.path.join("resources", "budget_data.csv")

total_months = 0
net_total_amount = 0
greatest_increase_amount = 0
greatest_increase_month = ""
greatest_decrease_amount = 0
greatest_decrease_month = ""
previous_amount = 0
previous_change_amount = 0
total_change_amount = 0

with open(input_path) as csv_file: # open file

    csv_reader = csv.reader(csv_file, delimiter=",") # read file
    header = next(csv_reader) # header

    for row in csv_reader: # iteration 
        month = str(row[0])
        amount = int(row[1])

        total_months = total_months + 1
        net_total_amount = net_total_amount + amount

        change_amount = amount - previous_amount

        # finding greatest increase/decrease month/amount
        if change_amount > 0 and change_amount > greatest_increase_amount:
            greatest_increase_month = month
            greatest_increase_amount = change_amount
        elif change_amount < 0 and change_amount < greatest_decrease_amount:
            greatest_decrease_month = month
            greatest_decrease_amount = change_amount

        previous_amount = amount

# findig the change amount average
change_amount_average = (greatest_increase_amount + greatest_decrease_amount) / total_months

output_path = os.path.join("analysis", "pybank_results.txt") # create output file path

# Write in output file
with open(output_path, 'w') as output_file:
    result = f"""
Financial Analysis
----------------------------
Total Months: {total_months}
Total: ${net_total_amount}
Average  Change: ${change_amount_average}
Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase_amount})
Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease_amount})
"""
    output_file.write(result) # write
