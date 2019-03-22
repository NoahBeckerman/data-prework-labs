# Variables
points = [(4, 5), (-0, 2), (4, 7), (1, -3), (3, -2), (4, 5),
          (3, 2), (5, 7), (-5, 7), (2, 2), (-4, 5), (0, -2),
          (-4, 7), (-1, 3), (-3, 2), (-4, -5), (-3, 2),
          (5, 7), (5, 7), (2, 2), (9, 9), (-8, -9)]
Quad_1, Quad_2, Quad_3, Quad_4 = [], [], [], [] 
quad_count = 0 # counter for each loop to apply counted arrows to right quad
#Functions 
def distance_from_center(point): 
    x, y = point
    return (x**2 + y**2)**0.5 # gets the closest number and rounds up its point no matter the input (float or int) and returns (int)

#Quad_4 = positive x and negative y cords

# 1. Robin Hood is famous for hitting an arrow with another arrow. Did you get it?

unique_points = set(points) # Removes doubles from list[points], then makes a set of remaining unique points.
arrow_x2 = len(points) > len(unique_points) # boolean check to see if total shots is more than unique arrow points ( indicating arrow on top of another arrow is true or false)

print("Did Robin hit an arrow in the same place?: {0}".format(arrow_x2))
print("----------")

# 2. Calculate how many arrows have fallen in each quadrant.
for x, y in points: 
  if x>0 and y>0:  #Quad_1 = positive x and y cords
   Quad_1.append((x, y))
  if x<0 and y>0: #Quad_2 = negative x and positive y cords
   Quad_2.append((x, y))
  if x<0 and y<0: #Quad_3 = negative x and y cords
   Quad_3.append((x, y))
  if x>0 and y<0: #Quad_4 = positive x and negative y cords
   Quad_4.append((x, y))
        
Arrow_2_Quad_Cords = [len(Quad_1), len(Quad_2), len(Quad_3), len(Quad_4)]
for total_arrows in Arrow_2_Quad_Cords:
  quad_count += 1
  print("Arrows in Quadrant {0}: {1}".format(quad_count, total_arrows))
print("----------")

# 3. Find the point closest to the center. Calculate its distance to the center
# Defining a function that calculates the distance to the center can help.

distances_from_center = sorted(points, key=distance_from_center) # uses built in sorted option in python

closest_arrow = distances_from_center[0]# first sorted option is closest point
farthest_arrow = distances_from_center[-1] # last sorted option is farthest point

closest_arrow_distance = distance_from_center(closest_arrow) # uses function to calc distance
farthest_arrow_distance = distance_from_center(farthest_arrow) # uses function to calc distance

print("The closest arrow from center point: {0}\nThe farthest arrow from center point: {2}\nThe closest arrows distance from the center point: {1}\nThe farthest arrow's distance from the center point: {3}".format(closest_arrow, closest_arrow_distance, farthest_arrow, farthest_arrow_distance))
print("----------")

# 4. If the target has a radius of 9, calculate the number of arrows that 
# must be picked up in the forest.
out_of_bounds = [out for out in points if distance_from_center(out) > 9] # Checks if any cord in plots list is over 9(positive or negative)

for arrows in out_of_bounds: # loop for each arrow that is found and print
  print("OUT OF BOUNDS ARROW: {0}".format(arrows)) 
print("Total out of bounds arrows: {0}".format(len(out_of_bounds)))

#3/22/19