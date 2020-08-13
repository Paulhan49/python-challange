import os
import csv
#define variables
total_months = 0
total_revenue = 0
revenue_average = 0
revenue_change = 0
month_change = []
month_count = []
month =[]
# Path to collect data from the Resources folder
budget_path = os.path.join('Resource', '03-Python_Homework_Instructions_PyBank_Resources_budget_data.csv')

# Read in the CSV file
with open(budget_path, 'r') as csvfile:
    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    # Skip the header
    csvheader = next(csvreader)
    row = next (csvreader)
 
 # Set variables within rows
    total_months += 1
    total_revenue = int(row[1])
    previous_revenue = int(row[1])
    greatest_increase = int(row[1])
    greatest_decrease = int(row[1])
    greatest_increase_month = row[0]
    greatest_decrease_month = row[0]

# Start forloop
    for row in csvreader:

# Count number of months in file
        month.append(row[0])
        month_count = len(month)

# Count the total revnue
        total_revenue += int(row[1])

#Average the changes of the profits/losses over the entire timeframe
        revenue_change = int(row[1]) - previous_revenue
        month_change.append(revenue_change)
        previous_revenue = int(row[1])
        revenue_average = sum(month_change) / len(month_change)

# Find the greatest increase of profit, and list the date with correspond profit value
        if int(row[1]) > greatest_increase:
            greatest_increase = int(row[1])       
            greatest_increase_month = row[0]
# Find the greatest decrease of profit, and list the date with correspnd profit value
        if int(row[1]) < greatest_decrease:
            greatest_decrease = int(row[1])
            greatest_decrease_month = row[0]
    highest_revenue = max(month_change)
    lowest_revenue = min(month_change)  


#print statements
print(f"Financial Analysis")
print(f"------------------------")
print(f"Total Months: {month_count}")
print(f"Total: ${total_revenue}")
print(f"Average Change: {revenue_average}")
print(f"Greatest Inc in Profits: {greatest_increase_month}, {highest_revenue}")
print(f"Greatest Dec in Profits: {greatest_decrease_month}, {lowest_revenue}")



