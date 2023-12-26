import re

def parse_and_prepare_data():
    workflow, _ = open('input', 'r').read().split("\n\n")

    workflows = {}
    for line in workflow.split():
        part_name, rules = re.findall(r"(\w+)\{(.*)\}", line)[0]
        workflows[part_name] = rules.split(",")

    return workflows


def calculate_combinations(parts):
    total_combinations = 0
    for part_configuration in parts:
        part_combinations = 1
        for category_range in part_configuration.values():
            category_min, category_max = category_range
            category_combinations = category_max - category_min + 1
            part_combinations *= category_combinations

        total_combinations += part_combinations
    return total_combinations

def apply_rule(operator, threshold, part_category, conditional_part, current_part):
    if operator == '<':
        conditional_part[part_category] = (conditional_part[part_category][0], threshold - 1)
        current_part[part_category] = (int(threshold), current_part[part_category][1])
    elif operator == '>':
        conditional_part[part_category] = (int(threshold) + 1, conditional_part[part_category][1])
        current_part[part_category] = (current_part[part_category][0], int(threshold))

    
def process_rule(nodes, parts, rule, current_part):
    if ":" in rule:
        part_category, operator, threshold, next_workflow = re.findall(r"(\w)([><])(\d+):(\w+)", rule)[0]
        threshold = int(threshold)

        conditional_part = current_part.copy()

        apply_rule(operator, threshold, part_category, conditional_part, current_part)

        if next_workflow in ["A", "R"]:
            if next_workflow == "A":
                parts.append(conditional_part.copy())
        else:
            nodes.append((next_workflow, conditional_part.copy()))
    else:
        if rule in ["A", "R"]:
            if rule == "A":
                parts.append(current_part.copy())
        else:
            nodes.append((rule, current_part.copy()))


def main():
    workflows = parse_and_prepare_data()

    parts = []
    part = {"x": (1, 4000), "m": (1, 4000), "a": (1, 4000), "s": (1, 4000)}
    nodes = [("in", part)]
    while len(nodes) > 0:
        current_workflow, current_part = nodes.pop()
        for rule in workflows[current_workflow]:
            process_rule(nodes, parts, rule, current_part)

    print(calculate_combinations(parts))


if __name__ == "__main__":
    main()