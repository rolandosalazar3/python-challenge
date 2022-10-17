import os
import csv
import statistics

# Path to collect data from the Resources folder
budget_data_csv = os.path.join('Resources', 'budget_data.csv')

# Open and read csv
with open(budget_data_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    
    # Read the header row first to skip over header
    next(csv_reader)
    
    #Variable for total number of months in list
    total_months = 0
    
    #Create list to store csv data
    profit_losses = []

    # Read through each row of data after the header and store in dictionary and calculate total months in data set

    for row in csv_reader:

        profit_losses.append({"month": row[0], "amount": int(row[1]),"change": 0})
        total_months = total_months + 1

# Calculate changes between the months
#variable for prior value
last_value = profit_losses[0]["amount"]

#Loop through dictionary to set the change value for each data item
for i in range(total_months):
    profit_losses[i]["change"] = profit_losses[i]["amount"] - last_value
	#set the new previous amount value for the next loop
    last_value = profit_losses[i]["amount"]

# Calculate Total Amount
net_total_amount = sum(row['amount'] for row in profit_losses) 

# Calculate Total Amount of Change
total_change = sum(row['change'] for row in profit_losses)

# Calculate Average Amount of Change
average_change = round(total_change / (total_months-1), 2)

# Calculate Greatest Increase and Decrease of Change
gic = max(profit_losses, key=lambda x:x['change'])
gdc = min(profit_losses, key=lambda x:x['change'])


#Print Results of Financial Analysis
print("Financial Analysis")
print(" ")
print("----------------------------")
print(" ")
print("Total Months: " + str(total_months))
print(" ")
print("Total: $" + str(net_total_amount))
print(" ")
print("Average Change: $" + str(average_change))
print(" ")
print(f'Greatest Increase in Profits: {gic["month"]} (${gic["change"]})')
print(" ")
print(f'Greatest Decrease in Profits: {gdc["month"]} (${gdc["change"]})')

#Export results in a text document called budget_results.txt
budget_results = open("analysis/budget_results.txt", "w")
budget_results.write("Financial Analysis\n" + "\n" + "----------------------------\n" + "\n" + "Total Months: " + str(total_months) + "\n " + "\nTotal: $" + str(net_total_amount) + "\n " + "\nAverage Change: $" + str(average_change) + "\n " + "\nGreatest Increase in Profits: " + str(gic["month"]) + " ($" + str(gic["change"]) + ")" + "\n " + "\nGreatest Decrease in Profits: " + str(gdc["month"]) + " ($" + str(gdc["change"]) +")")