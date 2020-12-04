import csv
import os
csvpath = os.path.join('Resources', 'election_data.csv')
file_to_output = os.path.join("analysis", "election_analysis.txt")
total = 0
vote_count = []
candidate_votes = {}
winning_candidate = ""
count = 0
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)
    for line in csvreader:
        # print(". ", end=""),
        total = total + 1
        name = line[2]
        if name not in vote_count:
            vote_count.append(name)
            candidate_votes[name] = 0
        candidate_votes[name] = candidate_votes[name] + 1
with open(file_to_output, "w") as txt_file:
    results = (
        f"\n\nElection Results\n"
        f"xxxxxxxxxxxxxxxxxxxxxxxxx\n"
        f"Total Votes: {total}\n"
        f"xxxxxxxxxxxxxxxxxxxxxxxxx\n")
    print(results, end="")
    txt_file.write(results)
    for candidate in candidate_votes:
        votes = candidate_votes.get(candidate)
        vote_percentage = float(votes) / float(total) * 100
        if (votes > count):
            count = votes
            winner = candidate
        vote_count = f"{candidate}: {vote_percentage:.3f}% ({votes})\n"
        print(vote_count, end="")
        txt_file.write(vote_count)
    winning_candidate = (
        f"xxxxxxxxxxxxxxxxxxxxxxxxxx\n"
        f"Winner: {winner}\n"
        f"xxxxxxxxxxxxxxxxxxxxxxxxxx\n")
    print(winning_candidate)
    txt_file.write(winning_candidate)
