"""
Had to completely rewrite my code for part 2 due to optimisation issues
and just bad code in general (OOM). Had to lookup alot of guides and help
on Reddit to understand this issue more properly. Uses DP and bitwise operator
to check valves. Found a great tip about bitwise operations and bitmasks
on Reddit.
"""

def traverse_cavern(bit_mask, valve, minutes): # Recursive function to gather the maximal value of iteration
    if minutes == 0: # Iteration done recursively
        return 0

    iteration = bit_mask, valve, minutes

    if iteration in DP: # Caching, speeds up search
        return DP[iteration]

    flow = 0
    if valve in valve_ids:
        if (bit_mask & (2**valve_ids[valve])) != 0:
            rate = valve_flow_rates[valve]
            flow = max(flow, rate*(minutes - 1) + traverse_cavern(bit_mask ^ (2**valve_ids[valve]), valve, minutes - 1)) # ^ = bitwise XOR

    for cavern_path in cavern_paths[valve]:
        flow = max(flow, traverse_cavern(bit_mask, cavern_path, minutes - 1))

    DP[iteration] = flow # Caching
    return flow


input = open('input').read().split('\n')
valves = []
valve_ids = {}
cavern_paths = {}
valve_flow_rates = {}
DP = {}

# Prepare input
for valve in input:
    valve_id = valve[6:8]

    temp_3 = valve.split(';')
    flow_rate = int(temp_3[0][23:])
    next_valve = valve[24:].split(';')[1]
    next_valve = next_valve[23:].split(', ')

    temp_2 = []
    for value in next_valve:
        temp_2.append(value.strip())
    next_valve = temp_2

    valves.append((valve_id, flow_rate, next_valve))

# Prepare data
for valve, flow_rate, cavern_path in valves:
    cavern_paths[valve] = cavern_path
    valve_flow_rates[valve] = flow_rate

    if flow_rate:
        valve_ids[valve] = len(valve_ids)

# Prepares bitmasks. Use of bitmask DP for human and elephant where elephant is reversed order. Masks represent opened valves
higher = range(0, 2**len(valve_ids))
lower = reversed(higher)
incrementations = []
for i, element in enumerate(lower):
    incrementations.append((higher[i], element))

max_flow = 0
for (a, b) in incrementations:
    path = traverse_cavern(a, 'AA', 26) + traverse_cavern(b, 'AA', 26) # Human then Elephant
    max_flow = max(max_flow, path)

print(max_flow)
