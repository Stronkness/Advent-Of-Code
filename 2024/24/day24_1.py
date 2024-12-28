import re
from functools import cache

initial_values = {}
gate_definitions = {}

with open("large.in") as file:
    while match := re.match(r"(\w{3}): ([01])", file.readline()):
        wire, value = match.groups()
        initial_values[wire] = int(value)

    while match := re.match(r"(\w{3}) (\w{2,3}) (\w{3}) -> (\w{3})", file.readline()):
        input1, operator, input2, output = match.groups()
        gate_definitions[output] = (
            input1 if input1 < input2 else input2,
            operator,
            input2 if input1 < input2 else input1
        )

@cache
def evaluate_wire(wire):
    if wire in initial_values:
        return initial_values[wire]

    if wire in gate_definitions:
        input1, operator, input2 = gate_definitions[wire]
        value1 = evaluate_wire(input1)
        value2 = evaluate_wire(input2)

        match operator:
            case "AND":
                return value1 & value2
            case "XOR":
                return value1 ^ value2
            case "OR":
                return value1 | value2

    return 0

z_values = [evaluate_wire(f"z{i:02}") for i in range(100)]
result = sum(z << i for i, z in enumerate(z_values))

print(result)
