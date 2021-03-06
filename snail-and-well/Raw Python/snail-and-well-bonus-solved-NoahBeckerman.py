import statistics 

# Assign problem data to variables with representative names
# well height, daily advance, night retreat, accumulated distance
advance_cm, well_height_cm, night_retreat_cm, accumulated_distance_cm= [30, 21, 33, 77, 44, 45, 23, 45, 12, 34, 55], 125, 20, 0


# Assign 0 to the variable that represents the solution
days = 0 # Total days elapsed

# Write the code that solves the problem
for comp_day in advance_cm:  # counts each number in array and counts it as a day
#(1 full day)
    days += 1 # add day to counter
    accumulated_distance_cm += comp_day # add current dist travled in day and add to total moved distance
    if accumulated_distance_cm > well_height_cm: #if snail is over the well height break for loop
        break # exit loop via break
    else: # if not over well height snail = sleep so remove 20cm from total height
    #(1 full night)
        accumulated_distance_cm -= night_retreat_cm # night time draw back



# Print the result with print('Days =', days)
print('Days =', days)

# What is its maximum displacement in a day? And its minimum?
max_disp, mini_disp = max(advance_cm), min(advance_cm) #using python version of what was taught on lesson for google sheets
print("Maximum Displacment = {0} \nMinimum Displacement = {1}".format(max_disp, mini_disp))



# What is its average progress?
avrg_prog = sum(advance_cm)/len(advance_cm) # adding all distances travled and dividing them by the amount of numbers in array
print("Average Progress = {0}".format(avrg_prog))

# What is the standard deviation of your displacement during the day?
print("Standard Deviation = {0}".format(statistics.pstdev(advance_cm))) # Using imported statistics library from python to get the standard deviation.

#3/22/19