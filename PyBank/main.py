#Import modules
import os
import csv

#Establish file path
csv_path = os.path.join("Resources","budget_data.csv")
#print(csv_path)

# Open the CSV
with open(csv_path) as csv_file:
    budget_data = csv.reader(csv_file, delimiter=",")
    #print(budget_data)
   
    #Count the number of rows in the data set, minus the header
    header = next(budget_data)
    #print(header)
    
    #define starting variables
    net_total=0
    months = []
    values = []
    
    #begin the for loop
    for row in budget_data:
        
        #add items to lists
        months.append(str(row[0]))
        values.append(int(row[1]))
        #print(months)
        #print(values)
   
        #Calculate net total:
        #read value from row[1] and cast as int
        monthly_net = int(row[1])
        #add amounts
        net_total = net_total + monthly_net
   
       
#calculate total number of months
total_months = len(months)

#calculate monthly value change and store to new list
value_change = []
for num in values:
    previous_num = values[values.index(num)-1]
    change_amount = num - previous_num
    #print(change_amount)
    value_change.append(int(change_amount))

#remove first value and replace with 0
#need to maintain same number of iterables as other lists
value_change.pop(0)
value_change.insert(0, int(0))
#print(value_change)

#calculate average change
sum_of_value_change = sum(value_change)
average_change = round(float(int(sum_of_value_change) / int(85)), 2)
#print(average_change)

#find greatest increase in profits
max_change = max(value_change)
#print(max_change)
#find list position of max change
max_pos = value_change.index(max_change)
#print(max_pos)
max_month = months[max_pos]
#print(max_month)

#find greatest decrease in profits
min_change = min(value_change)
min_pos = value_change.index(min_change)
min_month = months[min_pos]

print("Financial Analysis")
print("--------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: {max_month} (${max_change})")
print(f"Greatest Decrease in Profits: {min_month} (${min_change})")
       
        #find the greatest increase in profits from variables above

        #find the greatest decrease in profits from variables above

#As an example, your analysis should look similar to the one below:

#Financial Analysis
#----------------------------
#Total Months: 86
#Total: $38382578
#Average  Change: $-2315.12
#Greatest Increase in Profits: Feb-2012 ($1926159)
#Greatest Decrease in Profits: Sep-2013 ($-2196167)
#In addition, your final script should both print the 
# analysis to the terminal and export a text file with the results.