# %%
# import sys
# from collections import defaultdict, deque
# from typing import DefaultDict


# class BFSLeafCount():
#     def __init__(self, graph_data: DefaultDict[int, set]) -> None:
#         assert len(graph_data) > 0
#         self.graph_data = graph_data
#         self.visited = set()
#         self.queue = deque()
#         self.search_log = list()
#         self.leaf_counter = 0

#     def __search(self, start_vertex: int): # side effect
#         self.queue.append(start_vertex)
#         while len(self.queue) > 0:
#             vertex_visit = self.queue.popleft()
#             self.search_log.append(vertex_visit)
#             self.visited.add(vertex_visit)
#             is_leaf = True
#             for vertex in sorted(self.graph_data[vertex_visit]):
#                 if vertex in self.visited:
#                     continue
#                 else:
#                     is_leaf = False
#                     self.visited.add(vertex)
#                     self.queue.append(vertex)
#             if is_leaf:
#                 self.leaf_counter += 1

#     def search(self, start_vertex: int) -> list:
#         self.__search(start_vertex)
#         assert len(self.search_log) > 0
#         return self.search_log
    
#     def count_leaf(self, start_vertex: int = 1) -> int:
#         self.__search(start_vertex)
#         assert len(self.search_log) > 0
#         return self.leaf_counter


# N, W = map(int, input().split())
# case_in = sys.stdin.read().rstrip()
# edges = case_in.split('\n')


# graph_data: DefaultDict[int, set] = defaultdict(set)
# for edge in edges:
#     vertex_a, vertex_b = map(int, edge.split())
#     graph_data[vertex_a].add(vertex_b)
#     graph_data[vertex_b].add(vertex_a)


# bfs = BFSLeafCount(graph_data)
# print(W / bfs.count_leaf())




# %%
import sys
from collections import defaultdict


N, W = map(int, input().split())
case_in = sys.stdin.read().rstrip()
edges = case_in.split('\n')

graph_data = defaultdict(set)
for edge in edges:
    vertex_a, vertex_b = map(int, edge.split())
    graph_data[vertex_a].add(vertex_b)
    graph_data[vertex_b].add(vertex_a)

leaf_counter = 0
for node, edges in graph_data.items():
    if len(edges) == 1 and node != 1:
        leaf_counter += 1

print(W / leaf_counter)
# %%
# from collections import Counter


# N, W = map(int, input().split())
# case_in = open(0).read().split()
# if N == 2:
#     print(W)
# else:
#     counter = Counter(case_in)
#     c2 = Counter(Counter(case_in).values())[1]
#     if counter['1'] == 1:
#         print(W / (c2 - 1))
#     else:
#         print(W / c2)
# %%
# from collections import Counter as C
# N,W=map(int,input().split())
# c=C(open(0).read().split())
# c.pop('1')
# print(c)
# print(C(c.values()))
# d=C(c.values())[1]
# print(W/d)