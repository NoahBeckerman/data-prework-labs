# Assign problem data to variables with representative names
# well height, daily advance, night retreat, accumulated distance
well_height_cm = 125
daily_advance_cm = 30
night_retreat_cm = 20
accumulated_distance_cm = 0

# Assign 0 to the variable that represents the solution
days = 0

# Write the code that solves the problem
while (accumulated_distance_cm <= well_height_cm):
  days += 1 
  accumulated_distance_cm += daily_advance_cm 

  if accumulated_distance_cm >= well_height_cm:
    break 

  else:
    accumulated_distance_cm -= night_retreat_cm

# Print the result with print('Days =', days)
print('Days =', days)