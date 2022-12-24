"""
 For part two takes forever ... if the lazy method
 to just iterate through 10**12. But wouldn't work
 as memory would probably exceed and time is too 
 long. Intead there is a pattern in the input, there
 exist cycles. Save away these cycles and if the cycle
 appear again you check if the current cycle can end 
 the 10**12 iteration, then let math do the work to get
 answer.
"""

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
cycles = {}
idx = 0
res = 0

while True:
    # Check cycle and if 1000000000000 rocks has fallen
    height = int(max(p.imag for p in cavern))
    rock_jet = (idx % len(rocks), jet % len(jets))
    if rock_jet not in cycles:
        cycles[rock_jet] = (idx, height)
    else:
        prev_i, prev_h = cycles[rock_jet] # check if cycle appears
        if (1000000000000 - idx) % (idx - prev_i) == 0: # this is the check to see if 1000000000000 rocks has fallen, isch
            res = int((height + (1000000000000 - idx) / (idx - prev_i) * (height - prev_h)))
            break

    position = 1j * (height + 4)
    current_rock = rocks[idx % 5]
    while True:
        ROCK_move = 1 if jets[jet % len(jets)] == '>' else -1
        jet += 1
            
        valid = all(0 <= (coord + (position + ROCK_move)).real < 7 for coord in current_rock) and all(not c + (position + ROCK_move) in cavern for c in current_rock)
        if valid:
            position += ROCK_move
            
        valid = all(0 <= (coord + (position - 1j)).real < 7 for coord in current_rock) and all(not c + (position - 1j) in cavern for c in current_rock)
        if valid:
            position -= 1j
        else:
            cavern.update({c + position for c in current_rock})
            break
    idx += 1

print(res)
