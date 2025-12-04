rotations = open("test.in").read().splitlines()

start = 50
answer = 0

for rotation in rotations:
    turn, num = rotation[0], int(rotation[1:])

    answer += num // 100
    rem = num % 100

    if turn == 'L':
        if start - rem < 0:
            answer += 1
        start = (start - rem) % 100
    else:  # R
        if start + rem >= 100:
            answer += 1
        start = (start + rem) % 100

print(answer)
