import re, sympy

input = open("large.in").read().split("\n\n")
tokens = 0
for game in input:
    game = game.split("\n")
    A,B,PRIZE = [],[],[]
    for g in game:
        if g.startswith("Button A"):
            tmp_g = g.split("Button A: ")[1]
            split_str = re.findall(r'\d+', tmp_g)
            A = [int(split_str[0]), int(split_str[1])]
        elif g.startswith("Button B"):
            tmp_g = g.split("Button B: ")[1]
            split_str = re.findall(r'\d+', tmp_g)
            B = [int(split_str[0]), int(split_str[1])]
        else:
            tmp_g = g.split("Prize: ")[1]
            split_str = re.findall(r'\d+', tmp_g)
            PRIZE = [int(split_str[0]), int(split_str[1])]

    """
    Diophantine equation, the following equations comes from pen and paper,
    Basiclly it is:

    x * Ax + y * Bx - Px = 0
    x * Ay + y * By - Py = 0

    Then the Sympy library will solve this for us, it will find x and y
    """
    Ax = A[0]
    Ay = A[1]
    Bx = B[0]
    By = B[1]
    Px = PRIZE[0]
    Py = PRIZE[1]

    x, y = sympy.symbols('x y')
    result = sympy.solve([x * Ax + y * Bx - Px, x * Ay + y * By - Py])
    if (type(result[x]) or type(result[y])) == sympy.Rational:
        continue
    else:
        x_val = int(result[x])
        y_val = int(result[y])

        if (x_val or y_val) > 100:
            continue

        tokens += x_val*3 + y_val # X*3 + Y*1 apparently is mentioned in the task text

print(tokens)
    