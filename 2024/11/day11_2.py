from functools import cache # MEMOIZATION
from collections import defaultdict

input_data = open("large.in").read().split()
blinks = 0
stones = defaultdict(int)
for stone in input_data: # Store counts of each stone, not a expanded list as the same stones might appear more than once
    stones[int(stone)] += 1

@cache
def transform_stone(stone):
    print(stone)
    if stone == 0:
        return [1]
    elif stone >= 10 and len(str(stone)) % 2 == 0:
        stone_str = str(stone)
        stone_1, stone_2 = stone_str[:len(stone_str)//2], stone_str[len(stone_str)//2:]
        return [int(stone_1), int(stone_2)]
    else:
        return [stone * 2024]

while blinks < 75:
    blinks += 1
    new_stones = defaultdict(int)
    
    for stone, count in stones.items():
        transformed = transform_stone(stone)
        if len(transformed) == 1:
            new_stones[transformed[0]] += count
        else:
            new_stones[transformed[0]] += count
            new_stones[transformed[1]] += count
    
    stones = new_stones

print(sum(stones.values()))
