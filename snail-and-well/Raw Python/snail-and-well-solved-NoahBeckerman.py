# Assign problem data to variables with representative names
# well height, daily advance, night retreat, accumulated distance
well_height_cm = 125
daily_advance_cm = 30
night_retreat_cm = 20
accumulated_distance_cm = 0

# Assign 0 to the variable that represents the solution
days = 0

# Write the code that solves the problem

# While the total distance traveled is less than the well height continue looping
while (accumulated_distance_cm < well_height_cm):
#(1 day cycle)
  days += 1 # each loop adds a day to the counter (1 day cycle)
  accumulated_distance_cm += daily_advance_cm # add 30cm to total distance travled
  if accumulated_distance_cm > well_height_cm: # if the total distance travled is greater than the well height end the loop
    break # end loop via break
  else: # otherwise continue to night cycle
  #(1 night cycle)
    accumulated_distance_cm -= night_retreat_cm

    


# Print the result with print('Days =', days)
print('Days =', days)

# The total days elapsed is 11 because on the 10th night the snail drops to 100cm, the next morning the snail moves 30cm making a total of 130cm which is 5cm over the well height, thus removing the snail from the wells clutches!!!

#3/22/19