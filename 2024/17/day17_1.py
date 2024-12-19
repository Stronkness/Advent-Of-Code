import re

input = open("small.in").read()
ls = re.findall("\d+", input)
program = list(map(int, ls[3:]))
A,B,C = int(ls[0]),int(ls[1]),int(ls[2])

def run(program, A, B, C):
    out = []
    instruction_pointer = 0
    while instruction_pointer < len(program):
        literal = program[instruction_pointer+1]
        combo = 0

        # Get combo
        if literal < 4:
            combo = literal
        if literal == 4:
            combo = A
        if literal == 5:
            combo = B
        if literal == 6:
            combo = C

        # Start instructions
        if program[instruction_pointer] == 0: # adv
            A = int(A / 2**combo)
        elif program[instruction_pointer] == 1: # bxl
            B = B ^ literal
        elif program[instruction_pointer] == 2: # bst
            B = combo % 8
        elif program[instruction_pointer] == 3: # jnz
            if A != 0: instruction_pointer = literal - 2
        elif program[instruction_pointer] == 4: # bxc
            B = B ^ C
        elif program[instruction_pointer] == 5: # out
            out.append(combo % 8)
        elif program[instruction_pointer] == 6: # bdv
            B = int(A / 2**combo)
        elif program[instruction_pointer] == 7: # cdv
            C = int(A / 2**combo)

        instruction_pointer += 2
    return out

print(",".join(str(char) for char in run(program, A, B, C)))