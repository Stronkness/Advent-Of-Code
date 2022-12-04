import numpy as np

sections = open('input').read().split('\n')

wrong_pairs = 0
for section in sections:
    compartments = section.split(',')
    first_compartment, second_compartment = compartments[0], compartments[1]
    first_compartment = first_compartment.split('-')
    second_compartment = second_compartment.split('-')

    first_compartment = [x for x in range(int(first_compartment[0]), int(first_compartment[1]) + 1)]
    second_compartment = [x for x in range(int(second_compartment[0]), int(second_compartment[1]) + 1)]

    check_first = np.in1d(first_compartment,second_compartment)
    check_second = np.in1d(second_compartment,first_compartment)

    if all(check_first) or all(check_second):
        wrong_pairs += 1

print(wrong_pairs)