import os
import csv
#define variables
total_votes = 0
Khan_vote = 0
Correy_vote = 0
Li_vote = 0
Otooley_vote = 0
# Path to collect data from the Resources folder
election_path = os.path.join('Resource', 'election_data.csv')

# Read in the CSV file
with open(election_path, 'r') as csvfile:
    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    # Skip the header
    csvheader = next(csvreader)
    row = next (csvreader)
    
    # Setting variable
    vote = (row[0])
    candidate = (row[2])

    # Start forloop
    for row in csvreader:
        # Total number of vote cast
        total_votes += 1
        
        # Calaulate vote for each candidate
        if (row[2]) == "Khan":
            Khan_vote += 1
        elif (row[2]) == "Correy":
            Correy_vote += 1
        elif (row[2]) == "Li":
            Li_vote += 1
        else:
            Otooley_vote += 1

        #Calculate the win percentage for eace candiate
        Khan_percent = round(((Khan_vote / total_votes)* 100),2)
        Correy_percent = round(((Correy_vote / total_votes)* 100),2)
        Li_percent = round(((Li_vote / total_votes)* 100),2)
        Otooley_percent = round(((Otooley_vote / total_votes)*100),2)

        #Calculate the winner based on popular vote
        winner =  max(Khan_vote, Correy_vote, Li_vote, Otooley_vote)
       
        if winner == Khan_vote:
            winner_name = "Khan"
        elif winner == Correy_vote:
            winner_name = "Correy"
        elif winner == Li_vote:
            winner_name = "Li"
        else:
            winner_name = "O'Tooley" 

 # Print Result
print(f"Election Results")
print(f"---------------------------")
print(f"Total Votes: {total_votes}")
print(f"---------------------------")
print(f"Khan: {Khan_percent:}% ({Khan_vote})")
print(f"Correy: {Correy_percent}% ({Correy_vote})")
print(f"Li: {Li_percent}% ({Li_vote})")
print(f"O'Tooley: {Otooley_percent}% ({Otooley_vote})")
print(f"---------------------------")
print(f"Winner: {winner_name}")
print(f"---------------------------")       


# Export a text file with the results
election_result = os.path.join("Analysis", "election_data.txt")
with open(election_result, "w") as txtfile:
    txtfile.write(f"Election Results\n")
    txtfile.write(f"---------------------------\n")
    txtfile.write(f"Total Votes: {total_votes}\n")
    txtfile.write(f"---------------------------")
    txtfile.write(f"Khan: {Khan_percent:}% ({Khan_vote})\n")
    txtfile.write(f"Correy: {Correy_percent}% ({Correy_vote})\n")
    txtfile.write(f"Li: {Li_percent}% ({Li_vote})\n")
    txtfile.write(f"O'Tooley: {Otooley_percent}% ({Otooley_vote})\n")
    txtfile.write(f"---------------------------\n")
    txtfile.write(f"Winner: {winner_name}\n")
    txtfile.writer(f"---------------------------\n")   

