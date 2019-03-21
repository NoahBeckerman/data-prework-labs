import statistics 
# variables
stop_count = 0 # counter used in current person count display
stops = [(9, 0), (6, 3), (2, 6), (1, 0), (3, 1), (4, 5), (8, 4), (4, 5), (5, 10)] # random numbers and stops

print("---Bus Persons Calculator--")
# 1. Calculate the number of stops.
total_stops = len(stops)

print("Total number of stops: {0}".format(total_stops))
# 2. Assign a variable a list whose elements are the number of passengers in each stop: 
# Each item depends on the previous item in the list + in - out.
total_capacity= [0] # creating a blank array to count total persons on bus


for on, off in stops:  # loops for each stop in list
  total_capacity.append(total_capacity[-1]+on-off)# add to counter total number of persons on bus

total_capacity = total_capacity[1::] # removes the first 0 on list
print("-----------")


for current_persons_count in total_capacity: # displays list with current person count at stop #
  stop_count += 1 # counter for current stop with person count
  print("Stop: {0}\n - Person(s): {1}".format(stop_count, current_persons_count))


# 3. Find the maximum occupation of the bus.
max_persons = max(total_capacity)
print("-----------")
print("Maximum person(s) on bus: {0}".format(max_persons))


# 4. Calculate the average occupation. And the standard deviation.
avg_persons = sum(total_capacity)/len(total_capacity) # avg persons

print("-----------")
print("Average number of person(s) on bus: {0}".format(avg_persons))

print("-----------")
print("Standard Deviation for person(s): {0}".format(statistics.pstdev(total_capacity)))# Using imported statistics library from python to get the standard deviation.