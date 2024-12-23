import itertools
import networkx as nx

input_lines = open("large.in").read().split("\n")
graph = nx.Graph()
for line in input_lines:
    comp_1, comp_2 = line.strip().split("-")
    graph.add_edge(comp_1, comp_2)

cliques_of_three = set()
for comp_1, comp_2, comp_3 in itertools.combinations(graph.nodes, 3):
    if comp_1 in graph[comp_2] and comp_1 in graph[comp_3] and comp_2 in graph[comp_3]:
        cliques_of_three.add(comp_1 + comp_2 + comp_3)

result = 0
for connection in cliques_of_three:
    computer_1 = connection[:2]
    computer_2 = connection[2:4]
    computer_3 = connection[4:]
    if 't' in computer_1[0] or 't' in computer_2[0] or 't' in computer_3[0]:
        result += 1
print(result)
