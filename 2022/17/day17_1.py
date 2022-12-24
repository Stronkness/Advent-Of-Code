# Used complex number to represent the grid along with a set to store the cavern
jets = open('input').read()
rocks = [
    [(2 + 0j), (3 + 0j), (4 + 0j), (5 + 0j)],
    [(3 + 0j), (2 + 1j), (3 + 1j), (4 + 1j), (3 + 2j)],
    [(2 + 0j), (3 + 0j), (4 + 0j), (4 + 1j), (4 + 2j)],
    [(2 + 0j), (2 + 1j), (2 + 2j), (2 + 3j)],
    [(2 + 0j), (3 + 0j), (2 + 1j), (3 + 1j)]
    ]
"""
First row:
####

Second row:
.#.
###
.#.

Third row:
..#
..#
###

Fourth row:
#
#
#
#

Fifth row:
##
##
"""

jet = 0
cavern = set({grid_tile for grid_tile in range(7)}) # basiccly the 7 length size

for i in range(2022): # part 1 measurements
    height = int(max(p.imag for p in cavern)) # .imag gives the imaginary value
    position = 1j * (height + 4)
    current_rock = rocks[i % 5]
    while True:
        ROCK_move = 1 if jets[jet % len(jets)] == '>' else -1
        jet += 1
        
        valid = all(0 <= (coord + (position + ROCK_move)).real < 7 for coord in current_rock) and all(not c + (position + ROCK_move) in cavern for c in current_rock)
        if valid:
            position += ROCK_move
        
        valid = all(0 <= (c + (position - 1j)).real <= 6 for c in current_rock) and all(not c + (position - 1j) in cavern for c in current_rock)
        if valid:
            position -= 1j
        else:
            cavern.update({c + position for c in current_rock})
            break

print(int(max(p.imag for p in cavern)))
