# PyBank:  Python script for analyzing the financial records of your company
import os
import csv

input_path = os.path.join("resources", "election_data.csv")

total_votes = 0
khan_votes_percentage = 0
correy_votes_percentage = 0
li_votes_percentage = 0
tooley_votes_percentage = 0

winner_percentage = 0
winner_candidate = ""

candidates = {
    "Khan": 0,
    "Correy": 0,
    "Li": 0,
    "O'Tooley": 0
}

with open(input_path) as csv_file: # open file
    csv_reader = csv.reader(csv_file, delimiter=",") # read file
    header = next(csv_reader) # header

    for row in csv_reader: # iteration
        vote_id = int(row[0])
        country = str(row[1])
        candidate = str(row[2])

        total_votes = total_votes + 1

        if candidate in candidates:
            candidate_vote = candidates[candidate]
            candidate_vote = candidate_vote + 1
            candidates[candidate] = candidate_vote

# finding the candidate winner
khan_votes_percentage = round(candidates["Khan"] * 100 / total_votes, 3)
if khan_votes_percentage > winner_percentage:
    winner_candidate = "Khan"
    winner_percentage = khan_votes_percentage
correy_votes_percentage = round(candidates["Correy"] / total_votes * 100, 3)
if correy_votes_percentage > winner_percentage:
    winner_candidate = "Correy"
    winner_percentage = correy_votes_percentage
li_votes_percentage = round(candidates["Li"] / total_votes * 100,3)
if li_votes_percentage > winner_percentage:
    winner_candidate = "Li"
    winner_percentage = li_votes_percentage
tooley_votes_percentage = round(candidates["O'Tooley"] / total_votes * 100, 3)
if tooley_votes_percentage > winner_percentage:
    winner_candidate = "O'Tooley"
    winner_percentage = tooley_votes_percentage

output_path = os.path.join("analysis", "pypoll_results.txt")

# write in output file
with open(output_path, 'w') as output_file:
    result = f"""
Election Results
-------------------------
Total Votes: {total_votes}
-------------------------
Khan: {khan_votes_percentage}% ({candidates["Khan"]})
Correy: {correy_votes_percentage}% ({candidates["Correy"]})
Li: {li_votes_percentage}% ({candidates["Li"]})
O'Tooley: {tooley_votes_percentage}% ({candidates["O'Tooley"]})
-------------------------
Winner: {winner_candidate}
-------------------------
"""
    output_file.write(result) # write
