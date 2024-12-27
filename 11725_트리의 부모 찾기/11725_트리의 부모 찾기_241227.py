import sys


def solution(adj_list: list[list[int]]):
    parents = [0] * len(adj_list)

    def _dfs(start_v: int):
        nonlocal parents, adj_list
        stack = [start_v]
        visited = [False] * len(adj_list)
        while stack:
            v = stack.pop()
            visited[v] = True
            for next_v in adj_list[v]:
                if visited[next_v]:
                    continue
                parents[next_v] = v
                stack.append(next_v)

    _dfs(1)

    return "\n".join(map(str, parents[2:]))


if __name__ == "__main__":
    N = int(sys.stdin.readline().rstrip())
    edges = (tuple(map(int, e.split())) for e in sys.stdin.read().rstrip().split("\n"))
    adj_list: list[list[int]] = [[] for _ in range(N + 1)]
    for edge in edges:
        v1, v2 = edge
        adj_list[v1].append(v2)
        adj_list[v2].append(v1)

    print(solution(adj_list))
