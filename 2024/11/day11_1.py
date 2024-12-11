from functools import cache # MEMOIZATION

input_data = open("large.in").read().split()
blinks = 0
stones = [int(stone) for stone in input_data]

@cache
def transform_stone(stone):
    if stone == 0:
        return [1]
    elif stone >= 10 and len(str(stone)) % 2 == 0:
        stone_str = str(stone)
        stone_1, stone_2 = stone_str[:len(stone_str)//2], stone_str[len(stone_str)//2:]
        return [int(stone_1), int(stone_2)]
    else:
        return [stone * 2024]

while blinks < 25:
    blinks += 1
    new_stones = []
    
    for stone in stones:
        new_stones.extend(transform_stone(stone))
    
    stones = new_stones

print(len(stones))
