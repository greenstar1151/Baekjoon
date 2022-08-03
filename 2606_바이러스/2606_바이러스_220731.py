import sys
from collections import defaultdict, deque
from typing import DefaultDict


class BFS():
    def __init__(self, graph_data: DefaultDict[int, set]) -> None:
        assert len(graph_data) > 0
        self.graph_data = graph_data
        self.visited = set()
        self.queue = deque()
        self.search_log = list()

    def __search(self, start_vertex: int): # side effect
        self.queue.append(start_vertex)
        while len(self.queue) > 0:
            vertex_visit = self.queue.popleft()
            self.search_log.append(vertex_visit)
            self.visited.add(vertex_visit)
            for vertex in sorted(self.graph_data[vertex_visit]):
                if vertex in self.visited:
                    continue
                else:
                    self.visited.add(vertex)
                    self.queue.append(vertex)

    def search(self, start_vertex: int) -> list:
        self.__search(start_vertex)
        assert len(self.search_log) > 0
        return self.search_log
    


computer_count = int(input())
edge_count = int(input())
testcase_in = sys.stdin.read().rstrip()
edges = testcase_in.split('\n')



graph_data: DefaultDict[int, set] = defaultdict(set)
for edge in edges:
    vertex_a, vertex_b = map(int, edge.split())
    graph_data[vertex_a].add(vertex_b)
    graph_data[vertex_b].add(vertex_a)

bfs = BFS(graph_data)
print(len(bfs.search(1)) - 1)
