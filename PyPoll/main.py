import os
import csv

# code to collect data from source file
csvpath = os.path.join("Resources","election_data.csv")

total_votes = 0
votes_candidate = 0
winner = "name"
unique_words = []
output_list = []
count1 = 0
count2 = 0
count3 = 0
count4 = 0

# code to open, read and analyze data in source file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    unique_words = next(csvreader)
    first_row = next(csvreader)
    
 # code to capture all votes cast, candidate names and candidate number of votes received   
    for row in csvreader:
        total_votes += 1
        if row[2] == first_row[2]:
            count1 += 1
            cand1 = row[2]
        elif len(row[2]) < len(first_row[2]):
            count3 += 1
            cand3 = row[2]
        elif len(row[2]) > (len(first_row[2]) + 3):
            count4 += 1
            cand4 = row[2]
        elif len(row[2]) > (len(first_row[2])):
            count2 += 1
            cand2 = row[2]


# code to calculate percentage of vote
    #cand1Pct = round(((count1/total_votes)*100), 3)
    #cand2Pct = round(((count2/total_votes)*100), 3)
    #cand3Pct = round(((count3/total_votes)*100), 3)
    #cand4Pct = round(((count4/total_votes)*100), 3)     

# code to print and output election analysis

output=""
output+=(f"")
output+=(f"")
output+=(f'Election Results \n')
output+=(f"----------------------------- \n")
output+=(f'Total Votes: {total_votes} \n')
output+=(f"----------------------------- \n")
output+=(f'{cand1} : {((count1/total_votes)*100):.3f}% ({count1}) \n')
output+=(f'{cand2} : {((count2/total_votes)*100):.3f}% ({count2}) \n')
output+=(f'{cand3} : {((count3/total_votes)*100):.3f}% ({count3}) \n')
output+=(f'{cand4} : {((count4/total_votes)*100):.3f}% ({count4}) \n')
output+=(f"----------------------------- \n")
output+=(f"")

print(output)

# code to create path for output file
vote_output = os.path.join("Analysis","pypoll.txt")

# code to write output to output file
with open(vote_output, "w", newline="") as txtfile:
    txtfile.write(output)

