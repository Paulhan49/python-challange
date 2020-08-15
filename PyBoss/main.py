import os
import csv

# Output
file_to_output = "Analysis/employee_formatted.csv"

# Path to collect data from the Resources folder
employee_path = os.path.join('Resource', 'employee_data.csv')

#Setting variable 
First_name = []
Last_name = []
emp_ids = []
state_abbreviation = []
new_SSN_format = []
split_Name = []
split_DOB = []
split_SSN = []
    
# Read in the CSV file
with open(employee_path, 'r') as csvfile:
    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    # Skip the header
    csvheader = next(csvreader)

    # US states abbrevation in dictonary
    us_state_abbrev = {
        'Alabama': 'AL',
        'Alaska': 'AK',
        'Arizona': 'AZ',
        'Arkansas': 'AR',
        'California': 'CA',
        'Colorado': 'CO',
        'Connecticut': 'CT',
        'Delaware': 'DE',
        'Florida': 'FL',
        'Georgia': 'GA',
        'Hawaii': 'HI',
        'Idaho': 'ID',
        'Illinois': 'IL',
        'Indiana': 'IN',
        'Iowa': 'IA',
        'Kansas': 'KS',
        'Kentucky': 'KY',
        'Louisiana': 'LA',
        'Maine': 'ME',
        'Maryland': 'MD',
        'Massachusetts': 'MA',
        'Michigan': 'MI',
        'Minnesota': 'MN',
        'Mississippi': 'MS',
        'Missouri': 'MO',
        'Montana': 'MT',
        'Nebraska': 'NE',
        'Nevada': 'NV',
        'New Hampshire': 'NH',
        'New Jersey': 'NJ',
        'New Mexico': 'NM',
        'New York': 'NY',
        'North Carolina': 'NC',
        'North Dakota': 'ND',
        'Ohio': 'OH',
        'Oklahoma': 'OK',
        'Oregon': 'OR',
        'Pennsylvania': 'PA',
        'Rhode Island': 'RI',
        'South Carolina': 'SC',
        'South Dakota': 'SD',
        'Tennessee': 'TN',
        'Texas': 'TX',
        'Utah': 'UT',
        'Vermont': 'VT',
        'Virginia': 'VA',
        'Washington': 'WA',
        'West Virginia': 'WV',
        'Wisconsin': 'WI',
        'Wyoming': 'WY',
    }

    #Start for loop
    for row in csvreader:

        # append emp_id into list
        emp_ids.append(row[0])

        # Split Name column into first name and last name
        split_Name = row[1].split(" ")
        First_name = split_Name[0]
        Last_name = split_Name[1]

        # Rewrite DOB into MM/DD/YYYY format
        split_DOB = row[2].split("-")
        MM_DOB = split_DOB[1]
        DD_DOB = split_DOB[2]
        YYYY_DOB = split_DOB[0]
        DOB_format = MM_DOB + "/" + DD_DOB + "/" + YYYY_DOB
        
        # Rewrite first five SSN into ***-** format
        split_SSN = row[3].split("-")
        new_SSN_format = "***-**-" + split_SSN[2]
    
        # Abbreviate state into 2 -letter abbreviations.
        state_abbreviation = us_state_abbrev[row[4]]
        
#Zip all of the new lists together
boss_list = zip(emp_ids, First_name, Last_name, DOB_format, new_SSN_format, state_abbreviation)
            
# Use Zipfile and rewrite "employee_data.csv"
with open(file_to_output, "w", newline="") as datafile:
    writer = csv.writer(datafile)
    writer.writerow(["Emp ID", "First Names", "Last Names",
            "DOB", "SSN", "State"])
    writer.writerows(boss_list)
    





