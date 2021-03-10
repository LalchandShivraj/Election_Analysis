#The data we need to retrieve.
# 1. Total number of votes cast
# 2. A complete list of candidates who received votes
# 3. Total number of votes each candidate received
# 4. Percentage of votes each candidate won
# 5. The winner of the election based on popular vote
#
# Import the datetime class from the datetime module.
import datetime
import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")

# Initialize variables
# Open the election results and read the file.
total_votes = 0
winning_candidate = ""
winning_count = 0
winning_percentage = 0.0
candidate_options = []
candidate_votes = {}
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    
    # Read and print the header row
    headers = next(file_reader)
    print(headers)

    #Build a list of candidates while looping thru data, row by rom
    for row in file_reader:
        total_votes += 1
        candidate_name = row[2]
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
    
        candidate_votes[candidate_name] += 1
# 3. Print the total votes.
# Determine winning candidate, vote count and percentage of votes      
# Iterate through the candidate list.
for candidate_name in candidate_votes:
    votes = candidate_votes[candidate_name]
    vote_percentage = float(votes) / float(total_votes) * 100
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        winning_count = votes
        winning_percentage = vote_percentage
        winning_candidate = candidate_name
    #print(f"{candidate_name}: received {vote_percentage:.1f}% of the vote.")
    #  Print out the winning candidate, vote count and percentage to terminal
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)


#print(f'Total Votes =  {total_votes}')

#election_data = open(file_to_load, 'r')
# To do: perform analysis.

# Close the file.
election_data.close()

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using the open() function with the "w" mode we will write data to the file 
with open(file_to_save, "w") as txt_file:

# Write some data to the file.
#txt_file.write("Hello World")
# Write three counties to the file.
    txt_file.write("Counties in the Election")
    txt_file.write("\n------------------------")
    txt_file.write("\nArapahoe\nDenver\nJefferson")

# Close the file
txt_file.close()
