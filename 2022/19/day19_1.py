from collections import deque
from tqdm import tqdm

blueprints = []
information = open('input').read().split('\n')
result = 0

for info in information:
    info = info.split(' ')
    id = int(info[1][:-1])
    ore_robot_cost_ore = int(info[6])
    clay_robot_cost_ore = int(info[12])
    obsidian_robot_cost_ore = int(info[18])
    obsidian_robot_cost_clay = int(info[21])
    geode_robot_cost_ore = int(info[27])
    geode_robot_cost_obsidian = int(info[30])
    blueprints.append((id, ore_robot_cost_ore, clay_robot_cost_ore, obsidian_robot_cost_ore, obsidian_robot_cost_clay, geode_robot_cost_ore, geode_robot_cost_obsidian))

for blueprint in tqdm(blueprints):
    id, ore_robot_cost, clay_robot_cost, obsidian_robot_cost_ore, obsidian_robot_cost_clay, geode_robot_cost_ore, geode_robot_cost_obsidian = blueprint
    ore_cost_max = max(ore_robot_cost, clay_robot_cost, obsidian_robot_cost_ore, geode_robot_cost_ore)
    start = (1, 0, 0, 0, 0, 0, 0, 0, 24) # 24 is in minutes, and the 1 stands for one ore robot according to puzzle text
    q = deque([start])
    processed = set()
    max_geodes_blueprint = 0

    while q:
        ore_robots, clay_robots, obsidian_robots, geode_robots, ore, clay, obsidian, geode, minutes = q.pop()
        max_geodes_blueprint = max(max_geodes_blueprint, geode)

        if minutes == 0:
            continue

        ore = min(ore, ore_cost_max + (ore_cost_max - ore_robots) * (minutes - 1))
        clay = min(clay, obsidian_robot_cost_clay + (obsidian_robot_cost_clay - clay_robots) * (minutes - 1))
        obsidian = min(obsidian, geode_robot_cost_obsidian + (geode_robot_cost_obsidian - obsidian_robots) * (minutes - 1))

        state = (ore_robots, clay_robots, obsidian_robots, geode_robots, ore, clay, obsidian, geode, minutes)

        if state not in processed:
            processed.add(state)
        else:
            continue

        # This is basiclly a prioritation for the different robots. We go from building the most insignificant
        # robot to the most significant (Geode). As we only can build one robot per minute we add all robots we
        # can build and further up we pop the queue and the most significant robot of that minute is basiclly 
        # added to the next minute and is used in the math further up to fin max geodes later
        if ore >= ore_robot_cost and ore_robots < ore_cost_max:
            q.append((ore_robots + 1, clay_robots, obsidian_robots, geode_robots, ore - ore_robot_cost + ore_robots, clay + clay_robots, obsidian + obsidian_robots, geode + geode_robots, minutes - 1))
        if ore >= clay_robot_cost and clay_robots < obsidian_robot_cost_clay:
            q.append((ore_robots, clay_robots + 1, obsidian_robots, geode_robots, ore - clay_robot_cost + ore_robots, clay + clay_robots, obsidian + obsidian_robots, geode + geode_robots, minutes - 1))
        if ore >= obsidian_robot_cost_ore and clay >= obsidian_robot_cost_clay and obsidian_robots < geode_robot_cost_obsidian:
            q.append((ore_robots, clay_robots, obsidian_robots + 1, geode_robots, ore - obsidian_robot_cost_ore + ore_robots, clay - obsidian_robot_cost_clay + clay_robots, obsidian + obsidian_robots, geode + geode_robots, minutes - 1))
        if ore >= geode_robot_cost_ore and obsidian >= geode_robot_cost_obsidian:
            q.append((ore_robots, clay_robots, obsidian_robots, geode_robots + 1, ore - geode_robot_cost_ore + ore_robots, clay + clay_robots, obsidian - geode_robot_cost_obsidian + obsidian_robots, geode + geode_robots, minutes - 1))

        q.append((ore_robots, clay_robots, obsidian_robots, geode_robots, ore + ore_robots, clay + clay_robots, obsidian + obsidian_robots, geode + geode_robots, minutes - 1))

    result += id * max_geodes_blueprint

print(result)
