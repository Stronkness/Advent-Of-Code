game_action = open('input').read().split('\n')
list = []
for action in game_action:
    temp = []
    actions = action.split(' ')
    list.append(actions)

sum_score = 0
for game in list:
    elf = game[0]
    you = game[1]
    
    if you == 'X': # Lose
        if elf == 'A':
            sum_score += 3 # Scissors
        elif elf == 'B':
            sum_score += 1 # Rock
        else:
            sum_score += 2 # Paper     
    elif you == 'Y': # Draw
        if elf == 'A':
            sum_score += 1
        elif elf == 'B':
            sum_score += 2
        else:
            sum_score += 3
        sum_score += 3
    else: # Win
        if elf == 'A':
            sum_score += 2 # Paper
        elif elf == 'B':
            sum_score += 3 # Sissors
        else:
            sum_score += 1
        sum_score += 6

        

# Rock defeats Scissors, Scissors defeats Paper, and Paper defeats Rock. 
# If both players choose the same shape, the round instead ends in a draw.
# A = Rock , B = Paper , C = Scissors
# X = Rock , Y = Paper , Z = Scissors
# The score for a single round is the score for the shape you selected (1 for Rock, 2 for Paper, and 3 for Scissors) 
# plus the score for the outcome of the round (0 if you lost, 3 if the round was a draw, and 6 if you won). 

"""
    "Anyway, the second column says how the round needs to end: X means you need to lose, 
    Y means you need to end the round in a draw, and Z means you need to win. Good luck!"

    In the first round, your opponent will choose Rock (A), and you need the round to end in a draw (Y), so you also choose Rock. This gives you a score of 1 + 3 = 4.
    In the second round, your opponent will choose Paper (B), and you choose Rock so you lose (X) with a score of 1 + 0 = 1.
    In the third round, you will defeat your opponent's Scissors with Rock for a score of 1 + 6 = 7.

"""
print(sum_score)