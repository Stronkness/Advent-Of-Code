from string import ascii_lowercase, ascii_uppercase

rucksacks = open('input').read().split('\n')
total = 0

for rucksack in rucksacks:
    compartment_size = len(rucksack) / 2
    first_compartment, second_compartment = rucksack[:len(rucksack)//2], rucksack[len(rucksack)//2:]
    for element in first_compartment:
        if element in second_compartment:
            if element.islower():
                total += ascii_lowercase.index(element) + 1
                break
            else:
                total += ascii_uppercase.index(element) + 27
                break
print(total)
