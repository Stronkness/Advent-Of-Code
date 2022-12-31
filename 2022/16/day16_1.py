"""
Had to lookup alot of guides and help on Reddit to understand this issue more properly.
Uses DP and bitwise operator to check valves. Found a great tip about bitwise operations
and bitmaskson Reddit.
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

# Use of bitmask DP, masks represent opened valves
max_flow = traverse_cavern(((2**len(valve_ids)) - 1), 'AA', 30)

print(max_flow)
