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
        gandalf_score.append(True)
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
