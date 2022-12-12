import numpy as np

sections = open('input').read().split('\n')

def check_overlap(check):
    for x in check:
        if bool(x) is True:
            return True
    return False

overlap_pairs = 0
for section in sections:
    compartments = section.split(',')
    first_compartment, second_compartment = compartments[0], compartments[1]
    first_compartment = first_compartment.split('-')
    second_compartment = second_compartment.split('-')

    first_compartment = [x for x in range(int(first_compartment[0]), int(first_compartment[1]) + 1)]
    second_compartment = [x for x in range(int(second_compartment[0]), int(second_compartment[1]) + 1)]

    check = np.in1d(first_compartment,second_compartment)

    if check_overlap(check):
        overlap_pairs += 1

print(overlap_pairs)