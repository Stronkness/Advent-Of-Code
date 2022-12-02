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
    if you == 'X':
        sum_score += 1
    elif you == 'Y':
        sum_score += 2
    else:
        sum_score += 3

    if (elf == 'A' and you == 'X') or (elf == 'B' and you == 'Y') or (elf == 'C' and you == 'Z'):
        sum_score += 3
    
    if (you == 'X' and elf == 'C') or (you == 'Z' and elf == 'B') or (you == 'Y' and elf == 'A'):
        sum_score += 6
        

# Rock defeats Scissors, Scissors defeats Paper, and Paper defeats Rock. 
# If both players choose the same shape, the round instead ends in a draw.
# A = Rock , B = Paper , C = Scissors
# X = Rock , Y = Paper , Z = Scissors
# The score for a single round is the score for the shape you selected (1 for Rock, 2 for Paper, and 3 for Scissors) 
# plus the score for the outcome of the round (0 if you lost, 3 if the round was a draw, and 6 if you won). 
print(sum_score)