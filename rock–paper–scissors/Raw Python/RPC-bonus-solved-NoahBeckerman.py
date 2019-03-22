# Import the choice function of the random module
# https://stackoverflow.com/questions/306400/how-to-randomly-select-an-item-from-a-list
from random import choice

# Define a function that asks for an odd number on the keyboard, until it is not valid
# will keep asking
def GAME_COUNTER():
    global MAX_GAMES
    while True:
        MAX_GAMES = int(input("Please enter odd number to how many games to be played:\n> "))
        if MAX_GAMES %2 > 0:
            return(MAX_GAMES)
        else:
            print("PLEASE enter odd number to how many games to be played(please no even numbers)\n ")  

# Assign a list of 5 possible options.
OPTIONS = ['stone', 'paper', 'scissors', 'lizard', 'spock']

# Assign a variable to the number of games a player must win to win.
# Preferably the value will be based on the number of maximum games
MAX_WINS = GAME_COUNTER()// 2 + 1 # Best of of MAX_GAMES


# Define a function that randomly returns one of the 5 options.
# This will correspond to the play of the machine. Totally random.
def M_Choice_Func(selections=OPTIONS):
    return (choice(selections)) #Robot selection func that sets selections


# Define a function that asks your choice between 5
# you should only allow one of the 5 options. This is defensive programming.
# If it is not valid, keep asking until it is valid.
def U_Choice_Func(selections=OPTIONS):
    global U_Choice
    U_Choice = input("Please select an option: {0}, {1}, {2}, {3}, {4}\n> ".format(
        OPTIONS[0], OPTIONS[1], OPTIONS[2], OPTIONS[3], OPTIONS[4]))
    while U_Choice not in OPTIONS: #checks if they put in the write choice out of 3
        U_Choice = input("PLEASE select an option (case sensitive): {0}, {1}, {2}, {3}, {4}\n> ".format(OPTIONS[0], OPTIONS[1], OPTIONS[2], OPTIONS[3], OPTIONS[4]))
    else:
        return (U_Choice)


# Define a function that resolves a combat.
# Returns 0 if there is a tie, 1 if the machine wins, 2 if the human player wins
# Now there are more options
def Combat():
    if M_Choice == U_Choice: # if its a tie return 0
        return 0# sets rules for machine to win
    elif ((M_Choice == 'stone' and U_Choice == 'scissors') # sets rules for machine to win
          or (M_Choice == 'scissors' and U_Choice == 'paper')
          or (M_Choice == 'paper' and U_Choice == 'stone')
          or (M_Choice == 'spock' and U_Choice == 'stone')
          or (M_Choice == 'spock' and U_Choice == 'scissors')
          or (M_Choice == 'lizard' and U_Choice == 'spock')
          or (M_Choice == 'lizard' and U_Choice == 'paper')):
        return 1
    else: # Otherwise user wins 
        return 2


# Define a function that shows the choice of each player and the state of the game
# This function should be used every time accumulated points are updated
def Status():
    if outcome == 1: # if outcome fetched from Combat func == 1 machine won
        print("\nUser: {0}\nMachine: {1}\n - Machine has won!\n".format(U_Choice, M_Choice))
    elif outcome == 2:# vise versa
        print("\nUser: {0}\nMachine: {1}\n - User has won!\n".format(U_Choice, M_Choice))
    elif outcome == 0: # retuned tie
        print("\nUser: {0}\nMachine: {1}\n - It's a tie!\n".format(U_Choice, M_Choice))
    else:
        pass


# Create two variables that accumulate the wins of each participant
U_WIN = 0
M_WIN = 0

# Create a loop that iterates while no player reaches the minimum of wins
# necessary to win. Inside the loop solves the play of the
# machine and ask the player's. Compare them and update the value of the variables
# that accumulate the wins of each participant.
while (U_WIN < MAX_WINS and M_WIN < MAX_WINS): # while both opponents score is less then max wins then loop
    M_Choice = M_Choice_Func(OPTIONS) 
    U_Choice = U_Choice_Func()
    outcome = Combat()
    Status() # print checker
    if outcome == 1: #math to add to total score
        M_WIN += 1
    elif outcome == 2:
        U_WIN += 1
    else:
        pass


# Print by console the winner of the game based on who has more accumulated wins
def final_stats():
    if U_WIN >= MAX_WINS:
        print("\nThe User has won this battle!\n - Score: {0} - {1}".format(U_WIN, M_WIN))
    elif M_WIN >= MAX_WINS:
        print("\nThe Machine has won this battle!\n - Score: {0} - {1}".format(U_WIN, M_WIN))
    else:
        pass

final_stats() # line that initiates the dasiy chained function set.
