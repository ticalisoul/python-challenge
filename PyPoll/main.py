#import modules
import os
import csv

#set path of csv file
election_csv = os.path.join("..", "Resources", "election_data.csv")

#create list to store csv data
total_votes = 0

#dictionary to store candidate and vote count
election = {}

#open file, skip header, store data as rows in list
with open(election_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)
    
    for row in csvreader:
        total_votes += 1
        if row[2] in election.keys():
            election[row[2]] = election[row[2]] + 1
        else:
            election[row[2]] = 1
 
#empty lists to store data
candidates = []
vote_count = []

#fills empty list with key and value from dictionary
for key, value in election.items():
    candidates.append(key)
    vote_count.append(value)

#create vote percent list
percent = []
for i in vote_count:
    percent.append(round(i/total_votes*100, 2))

#zips name, vote count, and percent into one list to be printed
print_list = list(zip(candidates, vote_count, percent))

#store winner in list
winner_list = []

for name in print_list:
    if max(vote_count) == name[1]:
        winner_list.append(name[0])

winner = winner_list[0]
    
print("""
Election Results
-------------------------------
          """)
print("Total Votes: ", total_votes)
print("-------------------------------")
for entry in print_list:
    print(entry[0] + ": " + str(entry[2]) + "%  (" + str(entry[1]) + ")\n")
print("-------------------------------")
print("Winner: ", winner)
print("-------------------------------")

#create output path and file    
output_file = os.path.join("..", "Output", "pypoll.txt")

with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)
    datafile.write("Election Results\n")
    datafile.write("-------------------------------\n")
    datafile.write("Total Votes: " + str(total_votes) + "\n")
    datafile.write("-------------------------------" + "\n")
    for entry in print_list:
       datafile.write(entry[0] + ": " + str(entry[2]) + "%  (" + str(entry[1]) + ")\n")
    datafile.write("-------------------------------" + "\n")
    datafile.write("Winner: " + str(winner) + "\n")
    datafile.write("-------------------------------" + "\n")