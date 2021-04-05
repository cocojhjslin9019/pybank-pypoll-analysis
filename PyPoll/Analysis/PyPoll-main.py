import os
import csv
poll_data = os.path.join('..', 'Resource', 'PyPoll_Resources_election_data.csv')


total_votes = 0
candidates = []
voten = []
vote_per = []

with open(poll_data, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    header = next(csvreader)

    for row in csvreader:

        total_votes = total_votes + 1 

        if row[2] not in candidates:
            candidates.append(row[2])
            index = candidates.index(row[2])
            voten.append(1)
        else:
            index = candidates.index(row[2])
            voten[index] += 1
    
    for votes in voten:
        percentage = (votes/total_votes) * 100
        percentage = round(percentage)
        percentage = "%.3f%%" % percentage
        vote_per.append(percentage)
    
    winner = max(voten)
    index = voten.index(winner)
    winning_candidate = candidates[index]

print("Election Results")
print("--------------------------")
print(f"Total Votes: {str(total_votes)}")
print("--------------------------")
for i in range(len(candidates)):
    print(f"{candidates[i]}: {str(vote_per[i])} ({str(voten[i])})")
print("--------------------------")
print(f"Winner: {winning_candidate}")
print("--------------------------")


with open("PyPoll.txt","w") as txt_final:
	txt_final.write("Election Results")
	txt_final.write("\n")
	txt_final.write("------------------")
	txt_final.write("\n")
	txt_final.write(f"Total Votes:{str(total_votes)}")
	txt_final.write("\n")
	txt_final.write("------------------")
	txt_final.write("\n")
	for i in range(len(candidates)):
		txt_final.write(f"{candidates[i]}: {str(vote_per[i])} ({str(voten[i])})")
	txt_final.write("\n")
	txt_final.write("------------------")
	txt_final.write("\n")
	txt_final.write("Winner: {winning_candidate} ")
	txt_final.write("\n")
	txt_final.write("------------------")