def monkey_math(monkeys, monkey):
    math = monkey
    idx = monkeys.index(monkey)
    if str(math[1]).isdigit(): # is an int
        return monkeys
    else:
        first_term = math[1][0:4]
        operator = math[1][4]
        second_term = math[1][5:]
        
        terms = []
        while len(terms) != 2:
            for (x,y) in monkeys:
                if x == first_term:
                    terms.append((x,y))
                    break
            for (i,j) in monkeys:
                if i == second_term:
                    terms.append((i,j))
                    break
                
        first_term = terms[0][1]
        second_term = terms[1][1]

        if str(first_term).isdigit() and str(second_term).isdigit():
            if operator == '*':
                result = first_term * second_term
            elif operator == '/':
                result = int(first_term / second_term)
            elif operator == '+':
                result = first_term + second_term
            elif operator == '-':
                result = first_term - second_term

            monkeys.remove((math[0], math[1]))
            monkeys.insert(idx, (math[0], result))

    return monkeys

math = open('input').read().split('\n')
monkeys = []

for equation in math:
    equation = equation.split(' ')
    if equation[1].isdigit():
        monkeys.append((equation[0][:-1], int(equation[1])))
    else:
        monkeys.append((equation[0][:-1], ''.join(equation[1:])))

root = [(x,y) for x, y in monkeys if x  == "root"]

while(not str(root[0][1]).isdigit()):
    for monkey in monkeys:
        new = monkey_math(monkeys, monkey)
    root = [(x,y) for x, y in monkeys if x  == "root"]

print(root[0][1])
