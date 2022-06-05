import sys
from collections import defaultdict


n = int(input())
if n == 1: 
    print(0)
    sys.exit(0)
graph_data_in = sys.stdin.read().rstrip()
graph_data_in = graph_data_in.split('\n')

graph_data = [[] for _ in range(n+1)]
weight_data = defaultdict(int)
for line in graph_data_in:
    parent, child, weight = map(int, line.split())
    graph_data[parent].append(child)
    graph_data[child].append(parent)
    weight_data[( parent, child )] = weight
    weight_data[( child, parent )] = weight


def dfs(start_vertex):
    search_stack = [start_vertex]
    cost_space = [0 for _ in range(n+1)] 
    visited = set()
    while search_stack:
        node = search_stack.pop()
        visited.add(node)
        for next_node in graph_data[node]:
            if next_node in visited:
                continue
            else:
                cost_space[next_node] = cost_space[node] + weight_data[(node, next_node)]
                search_stack.append(next_node)

    max_cost = max(cost_space)
    return max_cost, cost_space.index(max_cost)

descending_max_cost, descending_max_cost_node = dfs(1)
asecnding_max_cost, asecnding_max_cost_node = dfs(descending_max_cost_node)

print(max(descending_max_cost, asecnding_max_cost))
