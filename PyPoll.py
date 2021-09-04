# Add dependencies
import csv
import os

# Assign a variable for the file to load and the path
file_to_load = os.path.join("resources", "election_results.csv")

#Create a filename variable to a direct path to the file
file_to_save = os.path.join("analysis", "election_analysis.txt")

# 1. Initialize total vote counter
total_votes = 0

# Create list for candidates
candidate_options = []
# Create a dictionary for candidate votes
candidate_votes = {}

#Open the election results and read the file.
with open(file_to_load) as election_data:
    
    # To do: read and analyze the data here
    file_reader = csv.reader(election_data)
     
    # Read header row
    header = next(file_reader)
     
    # Read and print rows in csv file
    for row in file_reader:
        # 2. Add to the total vote count.
        total_votes += 1  
        # Print Candidate name
        candidate_name = row[2]
        #If the candidates does not match any existing candidate...
        if candidate_name not in candidate_options:
            # Add candidate name to list
            candidate_options.append(candidate_name)
            
            # Track that candidates vote
            candidate_votes[candidate_name] = 0
            
        # Add a vote to candidate's count
        candidate_votes[candidate_name] += 1
# Interate through the candidate's list    
# Winning Candidate and Winning Count Tracker
    winning_candidate = ""
    winning_count = 0
    winning_percentage = 0
for candidate_name in candidate_votes:
    # Retrieve vote count of a candidate
    votes = candidate_votes[candidate_name] 
    # Calculate percent of votes
    vote_percentage = float(votes) / float(total_votes) * 100
    # Print candidate name and percent of votes
    print(f"{candidate_name} : received {vote_percentage:.1f}% of the vote\n")


    #Determin if the votes are greater than the winning count
    # 1. Determin if votes are greater that the winning count
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        # 2. If both are true then set winning_count = votes and winning_percent = vote_percent
        winning_count = votes
        winning_percentage = vote_percentage 
        # 3. Set winning_candidate to candidate's name
        winning_candidate = candidate_name
winning_candidate_summary = (
    f"--------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count: ,}\n"
    f"Winning Percentage: {winning_percentage: .1f}%\n"
    f"--------------------------\n")
print(winning_candidate_summary)