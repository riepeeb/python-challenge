import os
import csv

votescsv = os.path.join('Resources', 'election_data.csv')
output = os.path.join('Analysis', 'analysis.txt')

running = []
dd = []
ccs = []
rad = []

total_votes = 0

with open(votescsv) as file:
    csv_read = csv.reader(file, delimiter=',')
    headerline = next(csv_read)

    for row in csv_read:
        total_votes = total_votes + 1
        candidate = str(row[2])
        
        if candidate not in running:
            running.append(candidate)

        if candidate == "Diana DeGette":
            dd.append(candidate)

        if candidate == "Charles Casper Stockham":
            ccs.append(candidate)

        if candidate == "Raymon Anthony Doane":
            rad.append(candidate)

dd_total = len(dd)
ccs_total = len(ccs)
rad_total = len(rad)

dd_ratio = (dd_total / total_votes)*100
ccs_ratio = (ccs_total / total_votes)*100
rad_ratio = (rad_total / total_votes)*100

if dd_total > ccs_total and rad_total:
    winner = "Diana DeGette"

if ccs_total > dd_total and rad_total:
    winner = "Charles Casper Stockham"

if rad_total > ccs_total and dd_total:
    winner = "Raymon Anthony Doane"


print("Election Results")
print("----------------------------")
print(f"Total Votes {total_votes}")
print("----------------------------")
print(f"Charles Casper Stockham: {ccs_ratio:.3f}% ({ccs_total})")
print(f"Diana DeGette: {dd_ratio:.3f}% ({dd_total})")
print(f"Raymond Anthony Doana: {rad_ratio:.3f}% ({rad_total})")      
print("----------------------------")
print(f"Winner: {winner}")
print("----------------------------")

with open(output, "w") as txtfile:
    txtfile.write("Election Results \n")
    txtfile.write("---------------------------- \n")
    txtfile.write("Total Votes: " + str(total_votes) + "\n")
    txtfile.write("---------------------------- \n")
    txtfile.write("Charles Casper Stockham: " + str('{:0.3f}'.format(ccs_ratio))+ "%" + "(" + str(ccs_total) + ")" + "\n")
    txtfile.write("Diana DeGette: " + str('{:0.3f}'.format(dd_ratio))+ "%" + "(" + str(dd_total) + ")" + "\n")
    txtfile.write("Raymond Anthony Doane: " + str('{:0.3f}'.format(rad_ratio))+ "%" + "(" + str(rad_total) + ")" + "\n")
    txtfile.write("---------------------------- \n")
    txtfile.write(f"Winner: " + str(winner) + "\n")
    txtfile.write("---------------------------- \n")   
