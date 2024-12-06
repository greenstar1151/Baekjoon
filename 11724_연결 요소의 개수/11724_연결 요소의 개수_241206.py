import sys

sys.setrecursionlimit(1000 * 1000)


def solution(N: int, adj_list: list[list[int]]):
    visited = [0 for _ in range(N + 1)]
    component_num = 1

    def dfs(v: int):
        nonlocal visited, adj_list, component_num
        if visited[v] != 0:
            return False

        visited[v] = component_num
        for next_v in adj_list[v]:
            dfs(next_v)
        return True

    for i in range(1, N + 1):
        if dfs(i):
            component_num += 1

    return component_num - 1


if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().split())
    adj_list: list[list[int]] = [[] for _ in range(N + 1)]
    if N == 1:
        print(1)
        sys.exit(0)
    edges = sys.stdin.read().strip().split("\n")
    for e in edges:
        v1, v2 = map(int, e.split())
        adj_list[v1].append(v2)
        adj_list[v2].append(v1)

    print(solution(N, adj_list))
