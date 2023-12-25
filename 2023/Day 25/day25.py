import networkx

# Networkx is a great library for graph theory. I used it to find the minimum edge cut, which is the minimum number of
# edges that need to be removed to disconnect the graph. I then removed those edges from the graph and found the
# connected components. The number of connected components is the number of groups that can be formed. The number of
# elements in each group is the number of elements in each connected component. The total number of combinations is
# the product of the number of elements in each group.

graph = networkx.Graph()
file = open('input', 'r').read().splitlines()
for x in file:
    main_comp_split = x.split(': ')
    other_comp = main_comp_split[1].split(' ')

    main_comp = main_comp_split[0]
    for comp in other_comp:
        graph.add_edge(main_comp, comp)

minimum_cut = networkx.minimum_edge_cut(graph)
graph.remove_edges_from(minimum_cut)

remaining_components = list(networkx.connected_components(graph))
total = 1
for comp in remaining_components:
    total *= len(comp)

print(total)
