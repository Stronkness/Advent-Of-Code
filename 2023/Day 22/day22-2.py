from copy import deepcopy

def prepare_data():
    with open('input', 'r') as file:
        lines = file.read().strip().splitlines()

    prepared_bricks = []
    for index, line in enumerate(lines):
        stripped_line = line.strip()
        brick_coords1, brick_coords2 = stripped_line.split('~')
        x1, y1, z1 = map(int, brick_coords1.split(','))
        x2, y2, z2 = map(int, brick_coords2.split(','))

        brick_name = str(index)
        prepared_bricks.append((x1, y1, z1, x2, y2, z2, brick_name))
    
    return prepared_bricks

def is_brick_supported(brick, world):
    x_start, y_start, z_start, x_end, y_end, _, _ = brick
    support_level = z_start - 1

    if support_level == 0:
        return True

    for x in range(x_start, x_end + 1):
        for y in range(y_start, y_end + 1):
            if (x, y, support_level) in world:
                return True

    return False

def apply_gravity(bricks):
    bricks_fell = False
    updated_bricks = []
    support_surface = set()

    for (x_start, y_start, z_start, x_end, y_end, z_end, brick_name) in bricks:
        for x in range(x_start, x_end + 1):
            for y in range(y_start, y_end + 1):
                support_surface.add((x, y, z_end))

    for brick in bricks:
        x_start, y_start, z_start, x_end, y_end, z_end, brick_name = brick

        if not is_brick_supported(brick, support_surface):
            bricks_fell = True
            z_start -= 1
            z_end -= 1
            updated_brick = (x_start, y_start, z_start, x_end, y_end, z_end, brick_name)
            updated_bricks.append(updated_brick)
        else:
            updated_bricks.append(brick)

    return bricks_fell, updated_bricks

def calculate_block_falls(bricks):
    total_block_falls = 0
    stacked_bricks = set(bricks)

    for index, _ in enumerate(bricks):
        bricks_copy = deepcopy(bricks)
        del bricks_copy[index]
        bricks_fell = True

        while bricks_fell:
            bricks_fell, bricks_copy = apply_gravity(bricks_copy)

        new_stack = set(bricks_copy)
        total_block_falls += int((len(stacked_bricks ^ new_stack) - 1) / 2)

    return total_block_falls


def main():
    bricks = prepare_data()
    did_fall = True
    while did_fall:
        bricks = sorted(bricks, key=lambda x: x[2])
        did_fall, bricks = apply_gravity(bricks)

    print(calculate_block_falls(bricks))


if __name__ == '__main__':
    main()
