import sys
from collections import defaultdict, deque
from typing import DefaultDict



class DFS():
    def __init__(self, graph_data: DefaultDict[int, set]) -> None:
        assert len(graph_data) > 0
        self.graph_data = graph_data
        self.visited = set()
        self.search_log = list()

    def __search(self, vertex: int): # side effect
        self.search_log.append(vertex)
        self.visited.add(vertex)
        for vertex_visit in sorted(self.graph_data[vertex]):
            if vertex_visit in self.visited:
                continue
            else:
                self.__search(vertex_visit)

    def search(self, start_vertex: int) -> list:
        self.__search(start_vertex)
        assert len(self.search_log) > 0
        return self.search_log


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
    


N, M, V = map(int, input().split())
case_in = sys.stdin.read().rstrip()
edges = case_in.split('\n')



graph_data: DefaultDict[int, set] = defaultdict(set)
for edge in edges:
    vertex_a, vertex_b = map(int, edge.split())
    graph_data[vertex_a].add(vertex_b)
    graph_data[vertex_b].add(vertex_a)

dfs = DFS(graph_data)
print(' '.join(map(str, dfs.search(V))))
bfs = BFS(graph_data)
print(' '.join(map(str, bfs.search(V))))
