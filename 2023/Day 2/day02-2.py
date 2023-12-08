bag = open('input', 'r').read().splitlines()


S = 0
for game in bag:
    idx = int(game[5:game.index(':')])
    gm = game.split("Game {}: ".format(idx))[1]
    split_g = gm.split("; ")

    r, g, b = 0, 0, 0
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

        if cr > r:
            r = cr
        if cg > g:
            g = cg
        if cb > b:
            b = cb

    S += r*g*b

print(S) # Part 2
