# The data we need to retrieve
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote.

#Add our dependencies.

import csv

import os

#Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")

#Assign a variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

#1. Initialize a total vote counter.
total_votes = 0

#New List
candidate_options = []

#Open the election results and read th file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    #Read the header row.
    headers = next(file_reader)

    #Print each row in the CSV file.
    for row in file_reader:
        
        #2. Add to the total vote count.
        total_votes += 1

        #Print the candidate name for each row.
        candidate_name = row[2]

        #If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            
            #Add it to the lst of candidates
            candidate_options.append(candidate_name)
        
#3. Print the total votes.
print(candidate_options)

    

