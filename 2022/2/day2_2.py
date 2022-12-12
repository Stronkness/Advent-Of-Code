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

print(sum_score)