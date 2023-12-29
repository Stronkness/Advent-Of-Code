import math

class Module:
    def __init__(self, name, connection_type, destinations):
        self.name = name
        self.connection_type = connection_type
        self.destinations = destinations
        self.memory = self.initialize_memory()

    def initialize_memory(self):
        if self.connection_type == '%':
            return False
        elif self.connection_type == '&':
            return {}
        else:
            return None

    def receive_impulse(self, impulse, last_module):
        if self.connection_type == '%':
            self.memory = not self.memory
            return self.memory

        if self.connection_type == '&':
            self.memory[last_module] = impulse
            return not all(self.memory.values())

def load_connections(file_path):
    with open(file_path) as file:
        return [row.strip().split(' -> ') for row in file]

def create_modules(puzzle):
    modules = {}
    for module, destinations in puzzle:
        current_destinations = [dest.strip() for dest in destinations.split(',')]
        if module == 'broadcaster':
            modules[module] = Module('broadcaster', None, current_destinations)
        else:
            modules[module[1:]] = Module(module[1:], module[0], current_destinations)
    return modules

def connect_modules(modules):
    for current_module in modules.values():
        for destination in current_module.destinations:
            if destination not in modules:
                continue
            connected_module = modules[destination]
            if connected_module.connection_type != '&':
                continue
            connected_module.memory[current_module.name] = False


def calculate_cycle_lengths(modules):
    module_names = []
    for m in modules.values():
        if 'rx' in m.destinations:
            module_names.append(m.name)
    main_module_name = module_names[0]
    cycle_lengths = {m: 0 for m in modules[main_module_name].memory}

    for button_press in range(1, 10_000):
        if all(cycle_lengths.values()):
            break

        queue = []
        for destination in modules['broadcaster'].destinations:
            queue.append((destination, False, 'broadcaster'))

        while queue:
            current, impulse, last_module = queue.pop(0)

            if current not in modules:
                continue

            current_module = modules[current]

            if current_module.name == main_module_name and impulse:
                cycle_lengths[last_module] = button_press - cycle_lengths[last_module]

            if current_module.connection_type == '%' and impulse:
                continue

            impulse = current_module.receive_impulse(impulse, last_module)

            for next_destination in current_module.destinations:
                queue.append((next_destination, impulse, current_module.name))

    return math.lcm(*cycle_lengths.values())

def main():
    puzzle_input = load_connections("input")
    modules = create_modules(puzzle_input)
    connect_modules(modules)
    result = calculate_cycle_lengths(modules)
    print(result)

if __name__ == "__main__":
    main()
