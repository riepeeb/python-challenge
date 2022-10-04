import os

import csv

election_csv = os.path.join("..","python-challenge","PyPoll","Resources","election_data.csv")

candidates = []
votes = []
percent_votes = []
candidate_votes = 0
total_votes = 0
list_of_candidates = []
winner = ""
winner_votes = 0 


with open(election_csv) as csvfile: 
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

for row in csv_header: 
    # total_votes = total_votes +1

    name_candidate = row[2]
    votes.append(name_candidate)

    total_votes += 1 

    if list_of_candidates.count(name_candidate)==0:
        list_of_candidates.append(name_candidate)

print("-------------------------")
print("Election Results")
print("-------------------------")
print("Total Votes:" + str(total_votes))
print("-------------------------")

for name in list_of_candidates:
    candidate_votes= votes.count(name)

    percent_votes = candidate_votes/total_votes *100 

if winner_votes < candidate_votes:
    winner_votes = candidate_votes
    winner = name 

print(name + ": " + "% (" + str(candidate_votes)+ ")")
print("-------------------------")
print("Winner: " + winner)
print("-------------------------")



# Thinking Out Loud  

#     if name_candidate not in candidates:
#         candidates.append(name_candidate)
#         index= candidates.index(row[2])
#         votes.append(1)
#     else:
#         index = candidates.index(row[2])
#         votes[index] += 1

# for num_votes in votes:
#         percentage= (num_votes/total_votes) * 100
#         percentage= round(percentage)
#         percent_votes.append(percentage)

# winner= max(votes)
# index= votes.index(winner)
# winning_candidate = candidates[index]

# print("-------------------------")
# print("Election Results")
# print("-------------------------")
# print("Total Votes: " + str(total_votes))
# print("-------------------------")

# for i in range(len(candidates)):
#     print(f"{candidates[i]}: {str(percent_votes[i])} ({str(votes[i])})")
#     print(f"Winner: {winning_candidate}")
#     print("-------------------------")
# results= os.path.join("Output", "results.txt")


