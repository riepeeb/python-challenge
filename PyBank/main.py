import os
import csv

budgetcsv = os.path.join('Resources', 'budget_data.csv')
output = os.path.join('Analysis', 'analysis.txt')

pl_change = []
date = []
profit = []

open_profit = 0
months = 0

with open(budgetcsv) as fin:
    finread = csv.reader(fin, delimiter=',')

    headerline = next(finread)

    for row in finread:
        months = months + 1

        month_profit = int(row[1])
        month_change = month_profit - open_profit

        profit.append(month_profit)
        date.append(row[0])
        pl_change.append(month_change)

        open_profit = month_profit

remove_first_prof = pl_change.pop(0)
remove_first_date = date.pop(0)

pl_info = zip(date, pl_change)
total_change = sum(pl_change)
total_profit = sum(profit)
change_avg = float(total_change / len(pl_change))

greatnum = max(pl_change)
badnum = min(pl_change)

for month, change in pl_info:
    if change == greatnum:
        greatdate = month
    if change == badnum:
        baddate = month

print("Financial Analysis")
print("---------------------")
print(f"Total Months: {months}")
print(f"Total: ${total_profit}")
print(f"Average Change: ${change_avg:.2f}")
print(f"Greatest Increase in Profits: {greatdate} ({greatnum})")
print(f"Greatest Decrease in Profits: {baddate} ({badnum})")

with open(output, "w") as txtfile:
    txtfile.write("Financial Analysis\n")
    txtfile.write("---------------------\n")
    txtfile.write("Total Months:" + str(months) + "\n")
    txtfile.write("Total: $" + str(total_profit) + "\n")
    txtfile.write("Average Change: $" + str('{:0.2f}'.format(change_avg)) + "\n")
    txtfile.write("Greatest Increase in Profits:" + str(greatdate) + "(" + str(greatnum) + ")" + "\n")
    txtfile.write("Greatest Decrease in Profits:" + str(baddate) + "(" + str(badnum) + ")" + "\n")