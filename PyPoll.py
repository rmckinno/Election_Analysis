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
# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0
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
        # Save results to text file
with open(file_to_save, "w") as txt_file:
    election_results = (
        f'\nElection Results\n'
        f'-------------------------\n'
        f'Total Votes:{total_votes: ,}\n'
        f'-------------------------\n')
    print(election_results)
    txt_file.write(election_results)
    # Save final vote count to text file
    
    # Interate through the candidate's list    
    for candidate_name in candidate_votes:
        # Retrieve vote count of a candidate
        votes = candidate_votes[candidate_name] 
        # Calculate percent of votes
        vote_percentage = float(votes) / float(total_votes) * 100
        # Add candidate name and percent of votes to text file
        candidate_results = (f"{candidate_name} : {vote_percentage:.1f}% ({votes: ,})\n")
        
        # Print and write candidate's voter count and percentage
        print(candidate_results)
        txt_file.write(candidate_results)
        
        # Determin if votes are greater that the winning count
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            
            # If both are true then set winning_count = votes and 
            # winning_percent = vote_percent
            winning_count = votes
            winning_percentage = vote_percentage 
            
            # 3. Set winning_candidate to candidate's name
            winning_candidate = candidate_name
    
    #print(winning_candidate_summary)
    winning_candidate_summary = (
        f"--------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count: ,}\n"
        f"Winning Percentage: {winning_percentage: .1f}%\n"
        f"--------------------------\n")
    
    print(winning_candidate_summary)
    # Save the winning candidate's name to the text file
    txt_file.write(winning_candidate_summary)