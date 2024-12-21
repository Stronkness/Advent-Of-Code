from functools import cache
from random import random

NUMERIC_KEYPAD = {
    '7': 0, '8': 1, '9': 2,
    '4': 1j, '5': 1 + 1j, '6': 2 + 1j,
    '1': 2j, '2': 1 + 2j, '3': 2 + 2j,
    ' ': 3j, '0': 1 + 3j, 'A': 2 + 3j
}
CONTROL_SYMBOLS = {
    ' ': 0, '^': 1, 'A': 2, '<': 1j, 'v': 1 + 1j, '>': 2 + 1j
}

@cache
def calculate_path(start, end):
    """Calculate the shortest path between two keys."""
    pad = NUMERIC_KEYPAD if start in NUMERIC_KEYPAD and end in NUMERIC_KEYPAD else CONTROL_SYMBOLS
    diff = pad[end] - pad[start]
    dx, dy = int(diff.real), int(diff.imag)

    # Generate vertical and horizontal movements
    vertical_moves = ("^" * -dy) + ("v" * dy)
    horizontal_moves = ("<" * -dx) + (">" * dx)

    # Handle special case when crossing over the space key (' ')
    if pad[start] + dy * 1j == pad[' ']:
        return horizontal_moves + vertical_moves + "A"
    if pad[start] + dx == pad[' ']:
        return vertical_moves + horizontal_moves + "A"

    # Randomly decide movement order
    return (horizontal_moves + vertical_moves if random() < 0.5 else vertical_moves + horizontal_moves) + "A"

@cache
def calculate_length(code, depth, total_length=0):
    """Recursively calculate the total length of the path."""
    if depth == 0:
        return len(code)

    for i, char in enumerate(code):
        total_length += calculate_length(calculate_path(code[i - 1], char), depth - 1)

    return total_length

def solve_code(code, max_depth):
    """Solve a single code sequence for the given depth."""
    calculate_path.cache_clear()
    calculate_length.cache_clear()
    
    base_multiplier = int(code[:-1])
    return base_multiplier * calculate_length(code, max_depth)

def simulate_code(code, max_depth, simulations=100):
    """Simulate solving the code multiple times and return the minimum result. Not sure how many is required"""
    return min(solve_code(code, max_depth) for _ in range(simulations))

codes = open("large.in").read().split()
result = sum(simulate_code(code, 3) for code in codes)
print(result)
result = sum(simulate_code(code, 26) for code in codes)
print(result)
