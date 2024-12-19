from functools import cmp_to_key

def compare(a, b):
    if [a,b] in rules:
        return 1
    if [b,a] in rules:
        return -1
    else:
        return 0

input = open("large.in").read().split("\n\n")

rules = [list(map(int, row.split("|"))) for row in input[0].split("\n")]
updates = [[int(update) for update in upd.split(",")] for upd in input[1].split("\n")]
result = 0

for update in updates:
    valid = True
    for rule in rules:
        rule_1 = rule[0]
        rule_2 = rule[1]

        if rule_1 in update and rule_2 in update:
            if update.index(rule_1) >= update.index(rule_2):
                valid = False
                break
    
    if not valid:
        reordered_update = sorted(update, key=cmp_to_key(compare))
        result += reordered_update[len(reordered_update) // 2]

print(result)
