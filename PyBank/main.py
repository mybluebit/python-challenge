import os
import csv

# Location of budget_data.csv:
budget_csv = os.path.join ('Resources','budget_data.csv')

# Reading the csv file:
with open (budget_csv,'r',newline='') as budget:
	budget_reader = csv.reader (budget,delimiter=',')
	header = next(budget_reader)


	total = 0
	total_amount = 0
	proff_loss_1=0
	changes_1=0
	increase=0
	decrease=0
	sum = 0
	changes_list = []

	for row in budget_reader:

	#Calculating the Total Months:
		total+= 1

	#Calculating the Total Amount of Profit/Losses:
		total_amount += int(row[1])


	#Calculating the Changes of Profit/Losses:
		changes = int(row[1])-int(proff_loss_1)

	#Calculating the Greatest Increase in Profits:
		if (changes > increase):
			increase = changes
			date_increase=row[0]

	#Calculating the Greatest Decrease in Profits:
		if (changes < decrease):
			decrease = changes
			date_decrease=row[0]

		proff_loss_1 = row[1]
		changes_1 = changes

	#Creating a list of all Profit/losses Changes:
		changes_list.append(changes)

	#Calculating the total of Changes:
		sum += changes

	# Calculating the Average of Changes in Proft/Losses over the entire period.
	average =(sum - (int(changes_list[0]))) / (int(len(changes_list))-1)



# Printing Financial Analysis:
	print("Financial Analysis")
	print("-------------------------------")

# Printing Total Months:
	print(f"Total Months: {total}")

# Printing Total amount of Profit/Losses:
	print(f"Total: ${total_amount}")

# Printing the Average of Changes in Proft/Losses over the entire period:
	print (f"Average Changes: ${round((average),2)}")

# Printing the Greatest Increase in Profits:
	print (f"Greates Increase in Profits: {date_increase} (${increase})")

# Printing the Greatest Decrease in Losses:
	print (f"Greates Decrease in Losses: {date_decrease} (${decrease})")





# Location of Output file in txt format:
Pybank = os.path.join ('Exported_Analyze.txt')

# Location of Exported_Analyze.txt:
output = os.path.join ('Exported_Analyze.txt')

# Writing the output txt file:
with open (output,'w') as export:
  export.write("Financial Analysis\n")
  export.write("-------------------------------\n")

# Writing Total Months:
  export.write(f"Total Months: {total}\n")

# Writing Total amount of Profit/Losses:
  export.write(f"Total: ${total_amount}\n")

# Writing the Average of Changes in Proft/Losses over the entire period:
  export.write (f"Average Changes: ${round((average),2)}\n")

# Writing the Greatest Increase in Profits:
  export.write (f"Greates Increase in Profits: {date_increase} (${increase})\n")

# Writing the Greatest Decrease in Losses:
  export.write (f"Greates Decrease in Losses: {date_decrease} (${decrease})\n")
