import os
import csv
budget_data = os.path.join('..', 'Resource', 'budget_data.csv')

total_months = []
net_pl = []
profit_change = []

with open(budget_data, newline = "") as csvfile:
	csvreader = csv.reader(csvfile, delimiter = ",")
	header = next(csvreader)

	for row in csvreader:
		total_months.append(row[0])
		net_pl.append(int(row[1]))

	for i in range(len(net_pl)-1):
		profit_change.append(net_pl[i+1]-net_pl[i])

increase = max(profit_change)
decrease = min(profit_change)

monthly_increase = profit_change.index(max(profit_change))+1
monthly_decrease = profit_change.index(min(profit_change))+1

print("Financial Analysis")
print("------------------")
print(f"Total Months:{len(total_months)}")
print(f"Total:${sum(net_pl)}")
print(f"Average Chang:{round(sum(profit_change)/len(profit_change),2)}")
print(f"Greatest Increase in Profits:{total_months[monthly_increase]}(${(str(increase))}")
print(f"Greatest Decrease in Profits:{total_months[monthly_decrease]}(${(str(decrease))}")

with open("PyBank.txt","w") as txt_final:
	txt_final.write("Financial Analysis")
	txt_final.write("\n")
	txt_final.write("------------------")
	txt_final.write("\n")
	txt_final.write(f"Total Months:{len(total_months)}")
	txt_final.write("\n")
	txt_final.write(f"Total:${sum(net_pl)}")
	txt_final.write("\n")
	txt_final.write(f"Average Chang:{round(sum(profit_change)/len(profit_change),2)}")
	txt_final.write("\n")
	txt_final.write(f"Greatest Increase in Profits:{total_months[monthly_increase]}(${(str(increase))}")
	txt_final.write("\n")
	txt_final.write(f"Greatest Decrease in Profits:{total_months[monthly_decrease]}(${(str(decrease))}")