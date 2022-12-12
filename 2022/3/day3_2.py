from string import ascii_lowercase, ascii_uppercase

rucksacks = open('input').read().split('\n')
rucksacks = [rucksacks[i:i+3] for i in range(0, len(rucksacks), 3)]
total = 0

for rucksack in rucksacks:
    first_compartment, second_compartment, third_compartment = rucksack[0], rucksack[1], rucksack[2]
    for element in first_compartment:
        if element in second_compartment and element in third_compartment:
            if element.islower():
                total += ascii_lowercase.index(element) + 1
                break
            else:
                total += ascii_uppercase.index(element) + 27
                break
print(total)
