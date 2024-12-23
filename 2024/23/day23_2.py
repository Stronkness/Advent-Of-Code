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

largest_clique = max(nx.find_cliques(graph), key=len)
print(",".join(sorted(largest_clique)))
