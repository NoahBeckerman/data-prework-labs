import statistics 

# Assign problem data to variables with representative names
# well height, daily advance, night retreat, accumulated distance
advance_cm, well_height_cm, night_retreat_cm, accumulated_distance_cm= [30, 21, 33, 77, 44, 45, 23, 45, 12, 34, 55], 125, 20, 0

# Assign 0 to the variable that represents the solution
days = 0 

# Write the code that solves the problem
for comp_day in advance_cm:  

    days += 1
    accumulated_distance_cm += comp_day 

    if accumulated_distance_cm > well_height_cm: 
        break 
        
    else: 
        accumulated_distance_cm -= night_retreat_cm 

# Print the result with print('Days =', days)
print('Days =', days)

# What is its maximum displacement in a day? And its minimum?
max_disp, mini_disp = max(advance_cm), min(advance_cm) 
print("Maximum Displacment = {0} \nMinimum Displacement = {1}".format(max_disp, mini_disp))

# What is its average progress?
avrg_prog = sum(advance_cm[0:days])/days
print("Average Progress = {:3.2f}".format(avrg_prog))

# What is the standard deviation of your displacement during the day?
print("Standard Deviation = {:3.2f}".format(statistics.pstdev(advance_cm[0:days])))