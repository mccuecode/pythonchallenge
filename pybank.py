import csv

file_path = "/Users/markmccue/Downloads/budget_data_1.csv"

total_months = 0
total_revenue = 0
tot_rev = []

prev_revenue = 0
rev_change_list = []

greatest_incr = 0
greatest_decr = 99999999

with open(file_path) as revenue_data:
	reader = csv.DictReader(revenue_data)

	for row in reader:

		total_months = total_months + 1

		tot_rev.append(int(row["Revenue"]))

		

		revenue_change = int(row["Revenue"]) - prev_revenue 
		rev_change_list.append(revenue_change) 

		prev_revenue = int(row["Revenue"]) 

		if revenue_change > greatest_incr:
			greatest_incr = revenue_change
			greatest_incr_date = row["Date"]

		if revenue_change < greatest_decr:
			greatest_decr = revenue_change
			greatest_decr_date = row["Date"]

print('')
print('')
print("Financial Analysis For Data 1")
print("---------------------------")
print("The total number of months is " + str(total_months))
print("The total revenue is " + "$" + str(sum(tot_rev)))
avg_rev_change = sum(rev_change_list)/len(rev_change_list)
print("The average revenue change is $", avg_rev_change)
print("The greatest revenue increase is "  + "$" + str(greatest_incr) + " on " + str(greatest_incr_date))
print("The greatest revenue decrease is $" + str(greatest_decr) + " on " + str(greatest_decr_date))

import csv

file_path = "/Users/markmccue/Downloads/budget_data_2.csv"

total_months = 0
total_revenue = 0
tot_rev = []

prev_revenue = 0
rev_change_list = []

greatest_incr = 0
greatest_decr = 99999999

with open(file_path) as revenue_data:
	reader = csv.DictReader(revenue_data)

	for row in reader:

		total_months = total_months + 1

		tot_rev.append(int(row["Revenue"]))

		

		revenue_change = int(row["Revenue"]) - prev_revenue 
		rev_change_list.append(revenue_change) 

		prev_revenue = int(row["Revenue"]) 

		if revenue_change > greatest_incr:
			greatest_incr = revenue_change
			greatest_incr_date = row["Date"]

		if revenue_change < greatest_decr:
			greatest_decr = revenue_change
			greatest_decr_date = row["Date"]

print ('')
print ('')
print("Financial Analysis For Data 2")
print("---------------------------")
print("The total number of months is " + str(total_months))
print("The total revenue is " + "$" + str(sum(tot_rev)))
avg_rev_change = sum(rev_change_list)/len(rev_change_list)
print("The average revenue change is $", avg_rev_change)
print("The greatest revenue increase is "  + "$" + str(greatest_incr) + " on " + str(greatest_incr_date))
print("The greatest revenue decrease is $" + str(greatest_decr) + " on " + str(greatest_decr_date))