import os
import csv

#path to file
budget_csv = os.path.join("budget_data.csv")
#setting variables
total_months = 0
total_revenue = 0
changes =[]
date_count =[]
greatest_increase = 0
greatest_increase_month = 0
greatest_decrease = 0
greatest_decrease_month= 0
#opening the CSV
with open(budget_csv, newline = '') as budget_file:
    csvreader = csv.reader(budget_file, delimiter = ',')
    next(csvreader, None)
    row = next(csvreader)
# calculating months and revenue
    previous_profit = int(row[1])
    total_months = total_months + 1
    total_revenue = total_revenue + int(row[1])
    greatest_increase = int(row[1])
    greatest_increase_month = row[0]

    for row in csvreader:

        total_months = total_months + 1
        total_revenue = total_revenue + int(row[1])

        change = int(row[1]) - previous_profit
        changes.append(change)
        previous_profit = int(row[1])
        date_count.append(row[0])

        if int(row[1]) > greatest_increase:
            greatest_increase_month = row[0]
            greatest_increase = int(row[1])
        
        if int(row[1]) < greatest_decrease:
            greatest_decrease_month = row[0]
            greatest_decrease = int(row[1])
    
    avg_change = sum(changes)/len(changes)

    high = max(changes)
    low = min(changes)
#print terminal/gitbash text
    print("Financial Analysis")
    print("Total Months:" + str(total_months))
    print("Total Amount:" + str(total_revenue))
    print("Average Change: " + str(avg_change))
    print("Greatest Increase in Profits: " + str(greatest_increase_month) + str(max(changes)))
    print("Greatest Decrease in Profits: " + str(greatest_decrease_month) + str(min(changes)))
    
    #writing the output txt file

    PyBank = open("Fiancial_Analysis.txt", "w+")
    PyBank.write("Financial Analysis") 
    PyBank.write('\n' +"Total Months: " + str(total_months)) 
    PyBank.write('\n' +"Total Amount: " + str(total_revenue)) 
    PyBank.write('\n' +"Average: " + str(avg_change)) 
    PyBank.write('\n' +greatest_increase_month) 
    PyBank.write('\n' +str(high))
    PyBank.write('\n' +greatest_decrease_month) 
    PyBank.write('\n' +str(low))   
