import sympy as sp

# Symbolic variables
x, y, z = sp.symbols('x y z')
vx, vy, vz = sp.symbols('vx vy vz', positive=True, integer=True)

def expand_system(position, speed, system):
    px, py, pz = position
    sx, sy, sz = speed

    # Adding equations to the system
    equation1 = sp.Eq((px - vx) * (y - sy), (py - vy) * (x - sx))
    equation2 = sp.Eq((px - vx) * (z - sz), (pz - vz) * (x - sx))

    system.extend([equation1, equation2])

linear_system = []

with open('input', 'r') as file:
    for line in file:
        # Parsing position and speed from the input file
        position_str, speed_str = map(str.strip, line.split('@'))
        position = list(map(int, position_str.split(',')))
        speed = list(map(int, speed_str.split(',')))

        # Expanding the linear system
        expand_system(position, speed, linear_system)

solution = sp.solve(linear_system, [z, vz, y, vy, x, vx])

total = 0
for i, val in enumerate(solution[0]):
    if (i+1) % 2 == 0:
        total += val
print(total)
