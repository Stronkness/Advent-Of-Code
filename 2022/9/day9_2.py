def move_head(head, direction):
    hx, hy = head[0], head[1]
    if direction == 'U':
        hy += 1
    elif direction == 'D':
        hy -= 1
    elif direction == 'R':
        hx += 1
    elif direction == 'L':
        hx -= 1
    else:
        print("This shouldn't happen!")
    
    head = [hx, hy]
    return head

def move_tail(head, tail):
    hx, hy = head[0], head[1]
    tx, ty = tail[0], tail[1]
    diff_x = hx - tx
    diff_y = hy - ty
    if abs(diff_x) > 1 or abs(diff_y) > 1:
        sign = 0
        if diff_x > 0:
            sign = 1
        elif diff_x < 0:
            sign = -1
        tx += sign

        sign = 0
        if diff_y > 0:
            sign = 1
        elif diff_y < 0:
            sign = -1
        ty += sign

    tail = [tx, ty]
    return tail


instructions = open('input').read().split('\n')

head = [0,0] # Start position, overlapping with tail
tail = [[0,0] for i in range(9)]
visited = set() # Keeps unique lpositions saved

for move in instructions:
    direction, times = move.split(' ')

    for _ in range(int(times)):
        head = move_head(head, direction)

        for y in range(9):
            if y == 0:
                tail[y] = tuple(move_tail(head, tail[0]))
            else:
                tail[y] = tuple(move_tail(tail[y-1], tail[y]))
        visited.add(tail[len(tail)-1])

print(len(visited))