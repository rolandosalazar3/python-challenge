import os
import csv
import statistics

# Path to collect data from the Resources folder
election_data_csv = os.path.join('Resources', 'election_data.csv')

# Open and read csv
with open(election_data_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    
    # Read the header row first to skip over header
    next(csv_reader)
    
    #Variable for total number of votes in list
    total_votes = 0
    
    #Create variables to store vote count for candidates
    stockham = 0
    degette = 0
    doane = 0

    # Read through each row of data after the header and count the votes for each candidate and total votes

    for row in csv_reader:
        if row[2] == "Charles Casper Stockham":
            stockham = stockham + 1
        elif row[2] == "Diana DeGette":
            degette = degette + 1
        else: 
            doane = doane + 1
        total_votes = total_votes +1

#Create variables to store percentages for each candidate
stock_per = (stockham / total_votes) * 100
deg_per = (degette / total_votes) * 100
doa_per = (doane / total_votes) * 100
#Round variables to 3 decimal places\
stock_per = round(stock_per, 3)
deg_per = round(deg_per, 3)
doa_per = round(doa_per, 3)

#Calculate winner
if stock_per > deg_per and stock_per > doa_per:
    winner = "Charles Casper Stockham"
elif deg_per > stock_per and deg_per > doa_per:
    winner = "Diana DeGette"
else:
    winner = "Raymon Anthony Doane"

#Print Results of Election Analysis
print("Election Results")
print(" ")
print("-------------------------")
print(" ")
print("Total Votes: " + str(total_votes))
print(" ")
print("-------------------------")
print(" ")
print("Charles Casper Stockham: " + str(stock_per) + "% (" + str(stockham) +")")
print(" ")
print("Diana DeGette: " + str(deg_per) + "% (" + str(degette) +")")
print(" ")
print("Raymon Anthony Doane: " + str(doa_per) + "% (" + str(doane) +")")
print(" ")
print("-------------------------")
print(" ")
print("Winner: " + str(winner))
print(" ")
print("-------------------------")

#Export results in a text document called election_results.txt
election_results = open("analysis/election_results.txt", "w")
election_results.write("Election Results" + "\n\n-------------------------\n\n" + "Total Votes: " + str(total_votes) + "\n\n-------------------------\n\n" + "Charles Casper Stockham: " + str(stock_per) + "% (" + str(stockham) +")\n" + "\nDiana DeGette: " + str(deg_per) + "% (" + str(degette) +")\n" + "\nRaymon Anthony Doane: " + str(doa_per) + "% (" + str(doane) +")" + "\n\n-------------------------\n\n" + "Winner: " + str(winner) + "\n\n-------------------------")