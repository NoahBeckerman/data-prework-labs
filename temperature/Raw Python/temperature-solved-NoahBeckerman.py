import statistics 
# assign a variable to the list of temperatures
temperatures_C = [33,66,65,0,59,60,62,64,70,76,80,81,80,83,90,79,61,53,50,49,53,48,45,39]
temperatures_F = []
high_temp = []
high_temp_hours = []
Lowest_temp = min(temperatures_C)
Highest_temp = max(temperatures_C)
#Function for mean
def mean(x): 
    return sum(x)/(len(x))
    


# 1. Calculate the minimum of the list and print the value using print()
print("Lowest Temperature:\n{0}\n".format(Lowest_temp))

# 2. Calculate the maximum of the list and print the value using print()
print("Highest Temperature:\n{0}\n".format(Highest_temp))

# 3. Items in the list that are greater than 70ºC and print the result
print("High temperatures: ")
for temperature in temperatures_C: # for each number in list
  if temperature >= 70: # if temp is over or equal to 70ºC 
    high_temp.append(temperature) # add that temp to a list
for value in high_temp: # print list
    print(value, end=' ',)
print("\n")

# 4. Calculate the mean temperature throughout the day and print the result
print("Average Temperature:\n{0}\n".format(mean(temperatures_C)))

# 5.1 Solve the fault in the sensor by estimating a value
Estimated_Temp = (temperatures_C[2]+temperatures_C[4])/2 #List starts at 3:00 according to graph. and to find the estimated avrg, add all and divide by total.
print("Estimated Temp at {0} :\n{1}\n".format('3:00', Estimated_Temp))

# 5.2 Update of the estimated value at 03:00 on the list
print("Updated Temperatures: ")
temperatures_C[3] = Estimated_Temp # update list
for value in temperatures_C: # print list
    print(value, end=' ')
print("\n")

# Bonus: convert the list of ºC to ºFarenheit
print("Temperatures in Farenheit: ")
for temp in temperatures_C:
  temperatures_F.append((1.8 * temp + 32))# add to list
for value in temperatures_F: # print list
    print(value, end=' ')
print("\n")

# Print True or False depending on whether you would change the cooling system or not
if (len(high_temp) > 4  or Highest_temp > 80 or mean(temperatures_C) > 65): # if there is more than 4 hours of overcooling or temp reached over 80, or the avarage temp is past 65 change it.
    print("Cooling Status: WARNING!!! CHANGE SYSTEM!!!")
else:
    print("Cooling Status: Normal")
print("\n")


# 1. We want the hours (not the temperatures) whose temperature exceeds 70ºC
print("Hours of overheating: ")
for i, t in enumerate(temperatures_C):# for each temp in array
  if t>=70: #if temp is over or = to 70
    high_temp_hours.append(i) # add to list
for value in high_temp_hours:  # print list
    print(value, end=' ')
print("\n")

# 2. Condition that those hours are more than 4 consecutive and consecutive, not simply the sum of the whole set. Is this condition met?
hours_overheated_boolean = [True if t>=70 else False for t in temperatures_C] #creates a boolean that acts as a function/array to check if temp is over or = to 70 and sets it to true or false
for i, boolean in enumerate(hours_overheated_boolean): #for each value in boolean loop
  Overheat = False # each time it checks set the value to false
  if hours_overheated_boolean[i] == True and hours_overheated_boolean[i-1] == True and hours_overheated_boolean[i-2] == True and hours_overheated_boolean[i-3] == True:  # if all numbers in a span of 4 are set to true (indicating overheat for more than 4 hours at at a time) output a value to respond
    Overheat = True
    break
print("Overheating for more that {0} hours: {1}".format(4, Overheat))
print("\n")

# 3. Average of each of the lists (ºC and ºF). How they relate?
print("Average of ºC: {0}\nAverage of ºF: {1}".format(mean(temperatures_C), mean(temperatures_F)))
print("\n")

print("The mean of ºC: {0}\n - (Rounded: {1})\nThe mean of ºF: {1}".format((1.8 * mean(temperatures_C) + 32), mean(temperatures_F), round(1.8 * mean(temperatures_C) + 32)))


# 4. Standard deviation of each of the lists. How they relate?
print("Standard Deviation for ºC: {0}".format(statistics.pstdev(temperatures_C)))
# Using imported statistics library from python to get the standard deviation.
print("Standard Deviation for ºF: {0}".format(statistics.pstdev(temperatures_F)))
# Using imported statistics library from python to get the standard deviation.
print("\n")

#The Relation between them after you multiply ºC by '1.8' (converting to ºF) is the same.
print(" - ºF: {0}\n - ºC: {1}\n - Difference: {2}".format((statistics.pstdev(temperatures_F)), (statistics.pstdev(temperatures_C) * 1.8), (statistics.pstdev(temperatures_F) - (statistics.pstdev(temperatures_C) * 1.8))))
