import statistics
# 1. Spells now have a name and there is a dictionary that relates that name to a power.
# variables

POWER = {
    'Fireball': 50, 
    'Lightning bolt': 40, 
    'Magic arrow': 10, 
    'Black Tentacles': 25, 
    'Contagion': 45
}

gandalf = ['Fireball', 'Lightning bolt', 'Lightning bolt', 'Magic arrow', 'Fireball', 
           'Magic arrow', 'Lightning bolt', 'Fireball', 'Magic arrow', 'Fireball']
saruman = ['Contagion', 'Contagion', 'Black Tentacles', 'Fireball', 'Black Tentacles', 
           'Lightning bolt', 'Magic arrow', 'Contagion', 'Magic arrow', 'Magic arrow']

# Assign spell power lists to variables
gandalf_power = [POWER[spell_name] for spell_name in gandalf]
saruman_power = [POWER[spell_name] for spell_name in saruman]

# 2. A sorcerer wins if he succeeds in winning 3 spell clashes in a row.
gandalf_score = [] # win/loss keeper
saruman_score = [] # win/loss keeper

# Execution of spell clashes
print("--Lets start this battle!--")
for g_power, s_power in zip(gandalf_power, saruman_power): # loops for the total number of attacks
    if g_power > s_power: #if gandalf has stronger power he wins
        gandalf_score.append(True)
        saruman_score.append(False)
        print("Gandalf has won a clash!")
    elif g_power < s_power: #if Saruman has stronger power he wins
        gandalf_score.append(False)
        saruman_score.append(True)
        print("Saruman has won a clash!")
    else: #Otherwise its a tie
        gandalf_score.append(False)
        saruman_score.append(False)
        print("It's a tie!")
print("---------------------------")

# check for 3 wins in a row
for win in gandalf_score: # reads win/loss keeper and converts true to false to 1 or 0 for Gandalf
  if win == True:
    gandalf_string = ''.join('1')
  else: 
    gandalf_string = ''.join('0')

for win in saruman_score:# reads win/loss keeper and converts true to false to 1 or 0 for Saruman
  if win == True:
    saruman_string = ''.join('1')
  else: 
    saruman_string = ''.join('0')

gandalf_win = gandalf_string.find('111') # searches Gandalf for three consecutive wins
saruman_win = saruman_string.find('111') # searches Saruman for three consecutive wins

# check the winner
if gandalf_win > saruman_win: # if Gandalf returns three consecutive wins and results in a higher win ratio, print he has won
    print('Gandalf has won three times in a row!')
elif gandalf_win < saruman_win: # If Saruman returns three consecutive wins and results in a higher win ratio, print he has won
    print('Saruman has won three times in a row!')
# count sum of wins to losses
else: # Otherwise ( trick question) It counts the gross total of wins to losses and selects a winner
    if sum(gandalf_score) > sum(saruman_score): 
        print('Gandalf has won overall!')
    elif sum(gandalf_score) < sum(saruman_score): 
        print('Saruman has won overall!')
    else: 
        print('Tie')

# 3. Average of each of the spell lists.
g_avg =  sum(gandalf_power)/len(gandalf_power) # same as prior project
s_avg =  sum(saruman_power)/len(saruman_power) # same as prior project
print(" - Gandalf's Average Power: {0}\n - Saruman's Average Power {1}".format(g_avg, s_avg))
# 4. Standard deviation of each of the spell lists.
print(" - Standard Deviation for Gandalf = {0}".format(statistics.stdev(gandalf_power))) # Using imported statistics library from python to get the standard deviation.
print(" - Standard Deviation for Saruman = {0}".format(statistics.stdev(saruman_power)))
