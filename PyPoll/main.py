import os
import csv
#define variables
total_votes = 0
Kahn_vote = 0
Correy_vote = 0
Li_vote = 0
Otooley_vote = 0
# Path to collect data from the Resources folder
election_path = os.path.join('Resource', '03-Python_Homework_Instructions_PyPoll_Resources_election_data')

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
        if (row[2]) == "kahn":
            Khan_vote += 1
        elif (row[2]) == "Correy":
            Corey_vote += 1
        elif (row[2]) == "Li":
            Li_vote += 1
        else:
            Otooley_vote += 1

        #Calculate the win percentage for eace candiate
        Kahn_percent = Khan_vote / total_votes
        Correy_percent = Correy_vote / total_votes
        Li_percent = Li_percent / total_votes
        Otooley_percent = Otooley_vote / total_votes

        #Calculate the winner based on popular vote
        winner = max(Kahn_vote, Li_vote, Corey_vote, Otooley_vote)
        if winner == Kahn_vote:
            winner_name = "Kahn"
        elif winner == Li_vote:
            winner_name = "Li"
        elif winner == Correy_vote:
            winner_name = "Correy"
        else:
            winner_name = "O'Tooley"

 # Print Result
print(f"Election Results")
print(f"---------------------------")
print(f"Total Votes: {total_votes}")
print(f"---------------------------")
print(f"Kahn: {Kahn_percent:.3%}({Kahn_vote})")
print(f"Correy: {Correy_percent:.3%}({Correy_vote})")
print(f"Li: {Li_percent:.3%}({Li_vote})")
print(f"O'Tooley: {Otooley_percent:.3%}({Otooley_vote})")
print(f"---------------------------")
print(f"Winner: {winner_name}")
print(f"---------------------------")       



