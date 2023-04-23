#Import modules
import os
import csv

#Creating object out of data
csvpath=os.path.join('Resources','budget_data.csv')
csvpath

total_profit=0
total_change_profits=0
count=0
initial_profit=0
monthly_changes = []
dates=[]
profits=[]

with open(csvpath) as csvfile:
    csvreader=csv.reader(csvfile, delimiter=",")
    #print (csvreader)
    csv_header = next(csvreader)
    print(csv_header)

    #Reading first row and ahead
    first_row=next(csvreader)
    total_change_profits=int(first_row[1])
    final_profit=int(first_row[1])

    #Go through each row
    for row in csvreader:
        #Keep track of dates
        dates.append(row[0])
    

    #Total number of months
    count+=1

    #For greatest increase and decrease
    dates.append(row[0])

    #Append the profit information and calc. total profit
    profits.append(row[1])
    total_profit=total_profit+int(row[1])

    #Net Amount of Profit/Losses
    final_profit=int(row[1])
    monthly_change_profits=final_profit-initial_profit

    #Greatest Increase in profits
    greatest_increase=max(profits)
    greatest_index=profits.index(greatest_increase)
    greatest_date=dates[greatest_index]
                        
    #Greatest decrease
    greatest_decrease=max(profits)
    worst_index=profits.index(greatest_decrease)
    worst_date=dates[worst_index]

#Avg change in "Profit/Losses" over entire period
    average_change_profits=(total_change_profits/count)

 #Displaying information
    print("Financial Analysis")
    print("----------------------")
    print(f"Total Months: {str(count)}")
    print(f"Total: ${str(total_profit)}")
    print(f"Average Change: ${str(round(average_change_profits,2))}")
    print(f"Greatest Increase in Profits: {greatest_date} (${str(greatest_increase)})")
    print(f"Greatest Decrease in Profits: {worst_date} (${str(greatest_decrease)})")

#Exporing to .txt file
    output = open("output.txt", "w")

line1 = "Financial Analysis"
line2 = "---------------------"
line3 = str(f"Total Months: {str(count)}")
line4 = str(f"Total: ${str(total_profit)}")
line5 = str(f"Average Change: ${str(round(average_change_profits,2))}")
line6 = str(f"Greatest Increase in Profits: {greatest_date} (${str(greatest_increase)})")
line7 = str(f"Greatest Decrease in Profits: {worst_date} (${str(greatest_decrease)})")
output.write('{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(line1,line2,line3,line4,line5,line6,line7))
