# import sys
# from collections import defaultdict
# #from copy import deepcopy


# V = int(input())
# graph_data_in = sys.stdin.read().rstrip()
# graph_data_in = graph_data_in.split('\n')

# graph_data = defaultdict(set)
# weight_data = defaultdict(int)
# for line in graph_data_in:
#     node, *data, _ = line.split()
#     for i in range(len(data) // 2):
#         graph_data[int(node)].add(int(data[2 * i]))
#         weight_data[(int(node), int(data[2 * i]))] = int(data[2 * i + 1])


# def calc_cost(search_log):
#     cost = 0
#     for i in range(len(search_log)-1):
#         cost += weight_data[(search_log[i], search_log[i+1])]
#     return cost

# def dfs(start_vertex):
#     search_stack = [start_vertex]
#     visited = set()
#     visit_log = list()
#     max_cost = 0
#     max_cost_node = None
#     while search_stack:
#         node = search_stack.pop()
#         visited.add(node)
#         visit_log.append(node)
#         is_leaf = True
#         for next_node in graph_data[node]:
#             if next_node in visited:
#                 continue
#             else:
#                 is_leaf = False
#                 search_stack.append(next_node)
#         if is_leaf:
#             cost = calc_cost(visit_log)
#             if cost > max_cost:
#                 max_cost = cost
#                 max_cost_node = node
#             visit_log.pop()

#     return max_cost, max_cost_node

# descending_max_cost, descending_max_cost_node = dfs(1)
# #print(descending_max_cost, descending_max_cost_log)
# asecnding_max_cost, asecnding_max_cost_node = dfs(descending_max_cost_node)
# #print(asecnding_max_cost, asecnding_max_cost_log)

# print(max(descending_max_cost, asecnding_max_cost))

# %%
import sys
from collections import defaultdict


V = int(input())
graph_data_in = sys.stdin.read().rstrip()
graph_data_in = graph_data_in.split('\n')

graph_data = [[] for _ in range(V+1)]
weight_data = defaultdict(int)
for line in graph_data_in:
    node, *data, _ = line.split()
    for i in range(len(data) // 2):
        graph_data[int(node)].append(int(data[2 * i]))
        weight_data[( int(node), int(data[2 * i]) )] = int(data[2 * i + 1])


def dfs(start_vertex):
    search_stack = [start_vertex]
    cost_space = [0 for _ in range(V+1)] 
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
#print(descending_max_cost, descending_max_cost_log)
asecnding_max_cost, asecnding_max_cost_node = dfs(descending_max_cost_node)
#print(asecnding_max_cost, asecnding_max_cost_log)

print(max(descending_max_cost, asecnding_max_cost))
