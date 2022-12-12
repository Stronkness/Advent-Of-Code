import re

class Monkey:
    def __init__(self, number: int):
        self.monkey_id = number
        self.starting_items = []
        self.operation = ''
        self.test = ''
        self.if_true = ''
        self.if_false = ''
        self.inspected_items = 0

monkeys = open('input').read().split('\n\n')
monkey_buisness = [] # will be a list of lists containing the monkeys buisness, one list is a monkey

for monkey in monkeys:
    buisness = monkey.split('\n')

    monkey_id = int(buisness[0].strip()[-2]) # monkey "name"
    current_monkey = Monkey(monkey_id)

    match = re.split('(\d+)', buisness[1].strip())
    starting_items = [] # starting items for monkey
    for e in match:
        if e.isdigit():
            starting_items.append(int(e))
    current_monkey.starting_items = starting_items

    current_monkey.operation = buisness[2].strip().split("Operation: ")[1][6:] # operation when monkey checks item
    current_monkey.test = int(buisness[3].strip().split('Test: ')[1][13:]) # test to check which monkey to throw at
    current_monkey.if_true = int(buisness[4].strip().split('If true: ')[1][-1]) # throw to this monkey if true
    current_monkey.if_false = int(buisness[5].strip().split('If false: ')[1][-1]) # else this
    monkey_buisness.append(current_monkey)

for i in range(20): # time for monkey buissnes
    for monkey in monkey_buisness:
        while monkey.starting_items:
            item = monkey.starting_items.pop(0)
            monkey.inspected_items += 1
            worry_level = 0

            operation = monkey.operation
            if "old * old" in operation:
                worry_level = item*item
            elif "old +" in operation:
                op = int(operation[6:])
                worry_level = item + op
            elif "old *" in operation:
                op = int(operation[6:])
                worry_level = item * op

            worry_level = worry_level // 3
            if worry_level % monkey.test == 0:
                to = monkey.if_true
            else:
                to = monkey.if_false
            monkey_buisness[to].starting_items.append(worry_level)

inspected = []
for monkey in monkey_buisness:
    inspected.append(monkey.inspected_items)
inspected = sorted(inspected)
print(inspected[-1]*inspected[-2])
