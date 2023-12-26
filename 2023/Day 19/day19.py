import re

def parse_workflow(workflow_line):
    part_name, rules = re.match(r"(\w+)\{(.*)\}", workflow_line).groups()
    return part_name, rules.split(",")

def parse_ratings(parts_rating):
    matches = re.findall(r"(\w)=(\d+)", parts_rating)
    return {key: int(value) for key, value in matches}

def apply_workflow_rules(workflows, rating_dict, current_workflow):
    while current_workflow not in {'A', 'R'}:
        for rule in workflows[current_workflow]:
            if ":" in rule:
                part_category, operator, threshold, next_workflow = re.match(r"(\w)([><])(\d+):(\w+)", rule).groups()

                if ((operator == "<" and rating_dict[part_category] < int(threshold))
                        or (operator == ">" and rating_dict[part_category] > int(threshold))):
                    current_workflow = next_workflow
                    break
            else:
                current_workflow = rule

    return current_workflow

def main():
    workflow_data, ratings_data = open('input', 'r').read().split("\n\n")

    workflows = dict(parse_workflow(line) for line in workflow_data.split())
    ratings = ratings_data.split()

    total_rating = 0

    for parts_rating in ratings:
        rating_dict = parse_ratings(parts_rating)
        current_workflow = 'in'  # start part

        current_workflow = apply_workflow_rules(workflows, rating_dict, current_workflow)

        if current_workflow == "A":
            tmp = 0
            for _, value in rating_dict.items():
                tmp += value
            total_rating += tmp

    print(total_rating)

if __name__ == "__main__":
    main()
