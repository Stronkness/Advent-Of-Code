bag = open('input', 'r').read().splitlines()

r, g, b = 12, 13, 14


ids = set()
for game in bag:
    idx = int(game[5:game.index(':')])
    gm = game.split("Game {}: ".format(idx))[1]
    split_g = gm.split("; ")

    valid = True  # Assume the game is valid by default
    for gm in split_g:
        cr, cg, cb = 0, 0, 0
        s = gm.split()
        for i, c in enumerate(s):
            if 'red' in c:
                cr += int(s[i-1])
            elif 'green' in c:
                cg += int(s[i-1])
            elif 'blue' in c:
                cb += int(s[i-1])
        if cr > r or cg > g or cb > b:
            valid = False
            break

    if valid:
        ids.add(idx)

print(sum(set(ids))) # Part 1
