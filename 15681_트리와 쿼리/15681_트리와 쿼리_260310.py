import sys
from collections import deque

sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def make_tree(adj_list: list[list[int]], root: int = 1):
    tree: list[list[int]] = [[] for _ in range(len(adj_list))]
    visited = [False] * len(adj_list)
    q: deque[int] = deque()
    q.append(root)
    while q:
        n = q.popleft()
        if visited[n]:
            continue
        visited[n] = True
        for nn in adj_list[n]:
            if visited[nn]:
                continue
            tree[n].append(nn)
            q.append(nn)

    return tree


def solution(adj_list: list[list[int]], root: int, queries: list[int]):
    tree = make_tree(adj_list, root)

    subtree_sizes: list[int] = [1] * len(adj_list)

    def count_subtree_nodes(node: int):
        for child in tree[node]:
            count_subtree_nodes(child)
            subtree_sizes[node] += subtree_sizes[child]

    count_subtree_nodes(root)

    for query in queries:
        yield f"{subtree_sizes[query]}\n"


if __name__ == "__main__":
    N, R, Q = map(int, input().split())
    adj_list: list[list[int]] = [[] for _ in range(N + 1)]
    for _ in range(N - 1):
        u, v = map(int, input().split())
        adj_list[u].append(v)
        adj_list[v].append(u)
    queries = [int(input().strip()) for _ in range(Q)]
    sys.stdout.writelines(solution(adj_list, R, queries))
