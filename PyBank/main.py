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
    row_count=0
    net_total=0
    
    #begin the for loop
    for row in budget_data:
        #print(row)
        row_count = row_count + 1
        #print(row[1])
   
        #read value from row[1] and cast as int
        monthly_net = int(row[1])
        #add amounts
        net_total = net_total + monthly_net
   

    print(f"Total Months: {row_count}")
    print(f"Total: ${net_total}")

        #compare each month to the one before it,
        #calculate the difference, store as variable

        #find the average of the variables mentioned above

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