# Assign spell power lists to variables
gandalf = [10, 11, 13, 30, 22, 11, 10, 33, 22, 22]
saruman = [23, 66, 12, 43, 12, 10, 44, 23, 12, 17]

# Assign 0 to each variable that stores the victories
score_gandalf = 0
score_saruman = 0
total_matches = 0
# Execution of spell clashes
spell_options = range(len(gandalf)) # creates a range based on the total length of the gandalf list
for spell_power in spell_options: # for loop to start the clash
  if gandalf[spell_power] > saruman[spell_power]: # if gandalfs power is bigger than saurman, make gandalf the winner
    score_gandalf += 1 # add score to gandalfs total wins
    total_matches += 1 # counter for total matches
    print("Gandalf has won clash: {0}\n- Gandalf's power: {1}\n- Saruman's power: {2} \n".format(total_matches, gandalf[spell_power], saruman[spell_power])) # match status

  elif saruman[spell_power] > gandalf[spell_power]:# if saurman power is bigger than gandalf, make saurman the winner
    score_saruman += 1 # add score to saurman total wins
    total_matches += 1 # counter for total matches
    print("Saruman has won clash: {0}\n- Gandalf's power: {1}\n- Saruman's power: {2} \n".format(total_matches, gandalf[spell_power], saruman[spell_power])) # match status

  else:# otherwise its a draw
    total_matches += 1 # counter for total matches
    print("Clash was a draw!") # match status
    
# We check who has won, do not forget the possibility of a draw.
# Print the result based on the winner.
if score_gandalf > score_saruman: # assign the winner variable to who one based on total score ( Gandalf has more score here)
  winner = ("Gandalf")
elif score_gandalf < score_saruman: # assign the winner variable to who one based on total score ( Saruman has more score here)
    winner = ("Saruman")
else: # otherwise print its a draw
  print("NO ONE!!! It is a draw :)")


print("Total clashes: {0}\nGandalf's Wins: {1}\nSaurman's Wins: {2}\nVictor is: {3}".format(total_matches, score_gandalf, score_saruman, winner))# FINAL MATCH STATUS

#3/22/19
