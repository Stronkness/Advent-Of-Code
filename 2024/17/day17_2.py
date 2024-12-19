import re

input = open("large.in").read()
ls = re.findall("\d+", input)
program = list(map(int, ls[3:]))
A,B,C = 0,0,0

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


""" # ChatGPT wrote this comment section because I was too lazy to write it myself. 
The following code finds the smallest value of A such that the output of 
run(program, A+i, B, C) matches the last match_length elements of the program for 
increasing values of match_length. 

It iteratively tests values of A, adjusting its bits and iterating through 
possible values of i (from start_index to 7) until a match is found or match_length is reduced. 
If a match is found, A is updated, match_length is incremented to check a longer match, 
and the process repeats. If no match is found, match_length is decremented, and A is adjusted 
by shifting its bits to retry the search.

When register A is foudn that matches the last match_length elements of the program, the
value of A is printed.

TL;DR: This code finds the smallest value of A that will produce the output of the program 
starting with matching the tail of the program and working backwards to the head. 
"""
match_length = 1
start_index = 0

while match_length > 0 and match_length <= len(program):
    A = A * 8
    found_match = False
    for i in range(start_index, 8):
        output = run(program, A + i, B, C)
        if output == program[-match_length:]:
            found_match = True
            break

    if found_match:
        A = A + i
        match_length = match_length + 1
        start_index = 0
    else:
        match_length = match_length - 1
        A = A // 8
        start_index = (A % 8) + 1
        A = A // 8

print(A)

