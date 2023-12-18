
def create_differences(sequence):
    difference_matrix = []
    curr_row = sequence
    temp = []
    difference_matrix.append(sequence)

    while sum(curr_row) != 0:
        for i, num in enumerate(curr_row):
            if i == len(curr_row)-1:
                continue

            diff = curr_row[i+1] - num
            temp.append(diff)
        difference_matrix.append(temp)
        curr_row = temp
        temp = []

    return difference_matrix

def create_sequence_number(difference_matrix, part1=True):
    if part1:
        for r in difference_matrix:
            r.reverse()

    difference_matrix = list(reversed(difference_matrix))
    curr_depth = 0
    for i, row in enumerate(difference_matrix):
        if curr_depth == 0:
            row.insert(0, 0)
        else:
            row.insert(0, 0)
            temp = row[1] + difference_matrix[curr_depth-1][0] if part1 else row[1] - difference_matrix[curr_depth-1][0]
            row[0] = temp

        curr_depth += 1

    return difference_matrix[len(difference_matrix)-1][0]

seq = open('input', 'r').read().splitlines()
sequences = []
sequences = [[int(x) for x in s.split(' ')] for s in seq]

seq_numbers = []
for s in sequences:
    temp = []
    difference_matrix = create_differences(s)
    num = create_sequence_number(difference_matrix, part1=True)
    seq_numbers.append(num)

print(sum(seq_numbers))