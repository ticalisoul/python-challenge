import os
import csv

budget_csv = os.path.join("..", "Resources", "budget_data.csv") 

with open(budget_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)
    row_count = sum(1 for r in csvreader)
    for row in csvreader:
        total_revenue += int(row[1])
    print("""
Financial Analysis
-------------------------------
          """)
    print("Total Months: ", row_count)
    print("Total: ", total_revenue)
    