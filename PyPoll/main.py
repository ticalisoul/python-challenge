#import modules
import os
import csv

#set path of csv file
budget_csv = os.path.join("..", "Resources", "election_data.csv")

#create list to store csv data
months = []
profits = []
averages = []



#open file, skip header, store data as rows in list
with open(budget_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)
    for row in csvreader:
        months.append(row[0])
        profits.append(int(row[1]))
        
#calculate totals      
    total_months = len(months)
    total_revenue = sum(profits)

#set variables to find greatest increase, decrease, and average change   
    greatest_increase = profits[0]
    greatest_decrease = profits[0]
    previous_profit = 0    
 
#loop through list until conditionals are met   
    for i in range(len(profits)):
        if profits[i] >= greatest_increase:
            greatest_increase = profits[i]
            greatest_month = months[i]
        if profits[i] <= greatest_decrease:
            greatest_decrease = profits[i]
            least_greatest_month = months[i]
    for profit in profits:
        if previous_profit != 0:
            averages.append(int(profit - previous_profit))
        previous_profit = profit
    average = round(sum(averages)/total_months, 2)
    
        
    print("""
Election Results
-------------------------------
          """)
    print("Total Votes: ", )
    print("-------------------------------")
    print("Khan: ")
    print("Correy: ")
    print("Li: ")
    print("O'Tooley: ")
    print("-------------------------------")
    print("Winner: ")
    print("-------------------------------")

#create output path and file    
output_file = os.path.join("..", "Output", "pypoll.txt")

with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)
    datafile.write("Financial Analysis\n")
    datafile.write("-------------------------------\n")
    datafile.write("Average Change: " + "$" + str(average) + "\n")
    datafile.write("Greatest Increase in Profits: " + "$" + str(greatest_increase) + " " + greatest_month + "\n")
    datafile.write("Greatest Decrease in Profits: " + "$" + str(greatest_decrease) + " " + least_greatest_month + "\n")