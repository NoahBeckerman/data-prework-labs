# Assign spell power lists to variables
gandalf = [10, 11, 13, 30, 22, 11, 10, 33, 22, 22]
saruman = [23, 66, 12, 43, 12, 10, 44, 23, 12, 17]

# Assign 0 to each variable that stores the victories
score_gandalf = 0
score_saruman = 0

# Execution of spell clashes
for spell_power in range(len(gandalf)):

    if gandalf[spell_power] > saruman[spell_power]:
        score_gandalf += 1
        print(
            "Gandalf has won!\n- Gandalf's power: {0}\n- Saruman's power: {1} \n"
            .format(gandalf[spell_power], saruman[spell_power]))

    elif saruman[spell_power] > gandalf[spell_power]:
        score_saruman += 1
        print(
            "Saruman has won!\n- Gandalf's power: {0}\n- Saruman's power: {1} \n"
            .format(gandalf[spell_power], saruman[spell_power]))

    else:
        print("Clash was a draw!")

# We check who has won, do not forget the possibility of a draw.
# Print the result based on the winner.
if score_gandalf > score_saruman:
    winner = ("Gandalf")

elif score_gandalf < score_saruman:
    winner = ("Saruman")

else:
    winner = ("NO ONE!!! It is a draw :)")

print("Gandalf's Wins: {0}\nSaurman's Wins: {1}\nVictor is: {2}".format(
    score_gandalf, score_saruman, winner))
