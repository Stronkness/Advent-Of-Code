rotations = open("test.in").read().splitlines()

start = 50
answer = 0

for rotation in rotations:
    turn, num = rotation[0], int(rotation[1:])

    if turn == 'L':
        start = (start - num) % 100
    else:  # R
        start = (start + num) % 100

    if start == 0:
        answer += 1

print(answer)
