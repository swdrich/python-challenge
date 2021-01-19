#Import modules
import os
import csv

#Don't panic, something is happening.
print("Calcualting...")

#Establish file path
csv_path = os.path.join("Resources","election_data.csv")
#print(csv_path)

#read CSV
# Open the CSV
with open(csv_path) as csv_file:
    election_data = csv.reader(csv_file, delimiter=",")
    #print(election_data)
   
    #Count the number of rows in the data set, minus the header
    header = next(election_data)
    #print(header)

    #define values
    voter_ID = []
    county = []
    candidate_name = []

    #begin for loop
    for row in election_data:

        #add data to lists
        voter_ID.append(str(row[0]))
        county.append(str(row[1]))
        candidate_name.append(str(row[2]))
    #print(voter_ID)

# Calcualte the total number of votes cast
total_votes = len(voter_ID)
#print(total_votes)

#Get unique values from list and write to new list:
#geeksforgeeks.org/python-get-unique-values-list/
# function to get unique values 

unique_candidates = []
def unique(candidate_name): 
  
    # traverse for all elements 
    for x in candidate_name: 
        # check if exists in unique_list or not 
        if x not in unique_candidates: 
            unique_candidates.append(x) 
    # print list 
    #for x in unique_candidates: 
        #print (x)
    return unique_candidates    

unique(candidate_name)

print(unique_candidates)

 

#Print analysis to terminal:
print("Election Results")
print("--------------------------")
print(f"Total Votes: {total_votes}")
print("--------------------------")
#print(f"Total: ${net_total}")
#print(f"Average Change: ${average_change}")
#print(f"Greatest Increase in Profits: {max_month} (${max_change})")
#print(f"Greatest Decrease in Profits: {min_month} (${min_change})")


#Open export path for text file:
#tip o' the pin to this exchange: 
# https://stackoverflow.com/questions/5214578/print-string-to-text-file
output_path = os.path.join("Analysis", "PyPoll_Analysis.txt")

with open(output_path, "w") as text_file:

    print("Election Results", file = text_file)
    print("--------------------------", file = text_file)
    print(f"Total Votes: {total_votes}", file = text_file)
    print("--------------------------", file = text_file)
    #print(f"Total: ${net_total}", file = text_file)
    #print(f"Average Change: ${average_change}", file = text_file)
    #print(f"Greatest Increase in Profits: {max_month} (${max_change})", file = text_file)
    #print(f"Greatest Decrease in Profits: {min_month} (${min_change})", file = text_file)
       

# A complete list of candidates who received votes

# The percentage of votes each candidate won

# The total number of votes each candidate won

# The winner of the election based on popular vote.

# As an example, your analysis should look similar to the one below:

# Election Results
# -------------------------
# Total Votes: 3521001
# -------------------------
# Khan: 63.000% (2218231)
# Correy: 20.000% (704200)
# Li: 14.000% (492940)
# O'Tooley: 3.000% (105630)
# -------------------------
# Winner: Khan
# -------------------------
# In addition, your final script should both print the 
# analysis to the terminal and export a text file with the results.