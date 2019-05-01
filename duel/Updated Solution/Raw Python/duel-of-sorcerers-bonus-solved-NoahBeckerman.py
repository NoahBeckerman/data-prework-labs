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

gandalf = [
    'Fireball', 'Lightning bolt', 'Lightning bolt', 'Magic arrow', 'Fireball',
    'Magic arrow', 'Lightning bolt', 'Fireball', 'Magic arrow', 'Fireball'
]
saruman = [
    'Contagion', 'Contagion', 'Black Tentacles', 'Fireball', 'Black Tentacles',
    'Lightning bolt', 'Magic arrow', 'Contagion', 'Magic arrow', 'Magic arrow'
]

# Assign spell power lists to variables
gandalf_power = [POWER[spell_name] for spell_name in gandalf]
saruman_power = [POWER[spell_name] for spell_name in saruman]

# 2. A sorcerer wins if he succeeds in winning 3 spell clashes in a row.
gandalf_score = []
saruman_score = []

# Execution of spell clashes
print("--Lets start this battle!--")
for g_power, s_power in zip(gandalf_power, saruman_power):
    if g_power > s_power:
        gandalf_score.append(True)   #When you are using True and False for wins and losses here and then
                                     # converting them to 1's and 0's later, I think it is redundant as you can 
                                     # directly store 1's and 0's in the list. Also this is making the code more complicated
                # also the use of JOIN() is not what we want here, I think you are trying to replace the values TRUE with 1 and 
                # FALSE with 0. Please correct me if I am wrong
        saruman_score.append(False)
        for win in gandalf_score:
            if win == True:
                gandalf_string = ''.join('1')
            else:
                gandalf_string = ''.join('0')
        print("Gandalf has won a clash!")
    elif g_power < s_power:
        gandalf_score.append(False)
        saruman_score.append(True)
        for win in saruman_score:
            if win == True:
                saruman_string = ''.join('1')
            else:
                saruman_string = ''.join('0')
        print("Saruman has won a clash!")
    else:  #Otherwise its a tie
        gandalf_score.append(False)
        saruman_score.append(False)
        print("It's a tie!")
print("---------------------------")

gandalf_win = gandalf_string.find('111')
saruman_win = saruman_string.find('111')
# When we are comparing a string such as '111' in the whole list, we are not able to make this decision while the 
# competition is still going on, because you have already made the comparisons for all the clashes. For eg. if Gandalf 
# had won the first three clashes, we should have declared him a winner without trying to compare the next clashes. 
# Deos it make sense? 
                                               
                                             
# check the winner
if gandalf_win > saruman_win:
    print('Gandalf has won three times in a row!')
elif gandalf_win < saruman_win:
    print('Saruman has won three times in a row!')
else:
    if sum(gandalf_score) > sum(saruman_score):
        print('Gandalf has won overall!')
    elif sum(gandalf_score) < sum(saruman_score):
        print('Saruman has won overall!')
    else:
        print('It is a tie!')

# 3. Average of each of the spell lists.
g_avg = sum(gandalf_power) / len(gandalf_power)
s_avg = sum(saruman_power) / len(saruman_power)
print(
    " - Gandalf's Average Power: {:2.2f}\n - Saruman's Average Power {:2.2f}".
    format(g_avg, s_avg))
# 4. Standard deviation of each of the spell lists.
print(" - Standard Deviation for Gandalf = {:2.2f}".format(
    statistics.pstdev(gandalf_power)))
print(" - Standard Deviation for Saruman = {:2.2f}".format(
    statistics.pstdev(saruman_power)))


# TRY SOMETHING LIKE THIS 

# Change the values to test the code

'''
gandalf = ['Fireball', 'Fireball', 'Fireball', 'Magic arrow', 'Fireball', 
           'Magic arrow', 'Lightning bolt', 'Fireball', 'Magic arrow', 'Fireball']
saruman = ['Contagion', 'Contagion', 'Black Tentacles', 'Fireball', 'Black Tentacles', 
           'Lightning bolt', 'Magic arrow', 'Contagion', 'Magic arrow', 'Magic arrow']
           
SO here Gandalf should be declared winner right after the first three clashes and the competition ends!           
'''


'''
Total_wins_gandalf = 0
Total_wins_saruman = 0
counter1 = 0  # To check three consecutive victories for gandalf
counter2 = 0  # To check three consecutive victories for saruman
for each clash
    CHECK who wins it 
        Update counters and total wins values 
        CHECK if counter is 3 or not
            print("Winner")
            break
    Implement the else conditions as necessary
CHECK if counter is 3 again
    print("The competition ended after", X ,"clashes")
else:
    CHECK who won based on total number of wins 
        
'''       
# Again this is one solution , you can try something different as well. Try to keep the logc simple
