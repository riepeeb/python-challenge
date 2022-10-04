import os 

import csv

budget_csv = os.path.join("..","python-challenge","PyBank","Resources","budget_data.csv")

date = []
profit_losses = []
month = []
day = []
total_profit = []
profit_changes = 0
previous_value= 0 
greatest_increase = -999999999
greatest_decrease = 999999999


with open(budget_csv) as csvfile: 
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    for row in csvreader:
        date.append(row[0])

        profit_losses.append(int(row[1]))

        # split_month = row[0].split("-")
        # month.append(split_month[0])
        # day.append(split_month[1])
    

# The total number of months & profit/losses    
    # print(len(date))

# Net amt of profit/losses

total_profit_conv= [int(x) for x in profit_losses]
total_profit= sum(total_profit_conv)
# print (total_profit)

for i in range(len(profit_losses)-1):
    if profit_losses[i+1]-profit_losses[i]>greatest_increase:
        greatest_increase = i+1
    if profit_losses[i]-profit_losses[i+1]< greatest_decrease:
        greatest_decrease= i+1

print("Financial Analysis")

print ("--------------------")

print("Total Months: " + str(len(date)))

print("Total Profit/Losses: $" +  str(total_profit))

# print(f"Average Change: ${round(sum())}))

print(f"Greatest increase in Profits: ${greatest_increase}")

print(f"Greatest decrease in Profits: ${greatest_decrease}")

