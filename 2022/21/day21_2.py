"""
Part 2 requires help from sympy as to write this without help from sympy
requires alot of code and logic, and honestly I don't feel like to spend
that much time. Sympy uses linear solvers to get an equation and returns
an answer (expression). We mut set "humn" to a sympy symbol variable to 
do this and throw this expression into an online calculator. Using a 
recursive function to backtrack what root will look like (get the 
mathematical expressions of the component) is required here to gain 
this expression to solve. Sadly, code from part 1 needs to be rewritten
to work with this, or im just too tired ... Prefeerably with dict
"""

from sympy import symbols

# Goes from root and backwards to retrieve the mathematical expressions to get roots equation
def reverse_monkey_math(monkey, monkeys):
    monkey = monkeys[monkey]
    if type(monkey) == list:
        expr1 = reverse_monkey_math(monkey[0], monkeys) # first term
        expr2 = monkey[1] # operator
        expr3 = reverse_monkey_math(monkey[2], monkeys) # second term
        form = "({0} {1} {2})"
        equation = form.format(*(expr1,expr2,expr3)) # multiplication of expressions basiclly
        return equation
    return monkey # end of execution

math = open('input').read().split('\n')
monkeys = []

for equation in math:
    equation = equation.split(' ')

    if equation[0] == 'humn':
        monkeys.append(('humn', symbols('humn')))
        continue

    if equation[1].isdigit():
        monkeys.append((equation[0][:-1], equation[1]))
    else:
        monkeys.append((equation[0][:-1], ''.join(equation[1:])))

for monkey in monkeys:
    if monkey[0] == 'root':
        idx = monkeys.index(monkey)
        monkeys.remove(monkey)
        monkeys.insert(idx, (monkey[0], monkey[1][0:4] + '-' + monkey[1][5:])) # Basiclly expression = 0
        root = (monkey[0], monkey[1][0:4] + '-' + monkey[1][5:])

    if monkey[0] == 'humn':
        idx = monkeys.index(monkey)
        monkeys.remove(monkey)
        monkeys.insert(idx, (monkey[0], 'humn')) # Sympy symbol

temp = {} # Temporary solution, trying out things to see if it works. Easier to get values from a dict than a list
for monkey in monkeys:
    if monkey[1].isdigit():
        temp[monkey[0]] = monkey[1]
    elif monkey[1] == 'humn':
        temp[monkey[0]] = symbols('humn')
    else:
        temp[monkey[0]] = [monkey[1][0:4], monkey[1][4], monkey[1][5:]]
monkeys = temp

print(reverse_monkey_math('root', monkeys)) # Throw this expresion into an online calculator to view answer
# 3247317268284
