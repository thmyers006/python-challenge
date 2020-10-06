import os
import csv

# path to collect the source data from the budget data file
csvpath = os.path.join('Resources','budget_data.csv')

# declare all variables used in code
total_months = 0
grand_total = 0
profit_loss = 0 
avg_change = 0
g_increase = ["",0]
g_decrease = ["",9999999999]
previous = 0
seriouslyprevious = 0
avg_sum = 0

# code to open, read and analyze data in budget data file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    first_row = next(csvreader)

    for row in csvreader:
        total_months = total_months + 1
        if total_months == 1:
            seriouslyprevious = int(row[1])
        
        grand_total = grand_total + int(row[1])
        profit_loss = int(row[1]) - previous  
        previous = int(row[1])
        #print(profit_loss)
        avg_sum = avg_sum + profit_loss
        
# calculate the greatest increase, decrease and average change

        if profit_loss > g_increase[1]:
            g_increase[0] = row[0]
            g_increase[1] = profit_loss
            
        if profit_loss < g_decrease[1]:
            g_decrease[0] = row[0]
            g_decrease[1] = profit_loss
            
avg_sum = (avg_sum - seriouslyprevious)
avg_change = round((avg_sum)/(total_months - 1),2)


# code to print analysis
output = ""
output+=(f'')
output+=(f'Financial Analysis \n')
output+=(f'------------------------------------ \n')
output+=(f'Total Months : {total_months} \n')
output+=(f'Total: {grand_total} \n')
output+=(f'------------------------------------ \n')
output+=(f'Average Change: {avg_change} \n')
output+=(f'Greatest increase in Profits: {g_increase[0]} (${g_increase[1]}) \n')
output+=(f'Greatest decrease in Profits: {g_decrease[0]} (${g_decrease[1]}) \n')
output+=(f'')

print(output)

# code to create path for output file
data_output = os.path.join("Analysis","pybank.txt")

# code to write output to output file
with open(data_output, "w", newline="") as txtfile:
    txtfile.write(output)
    
