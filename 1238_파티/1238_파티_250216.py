import heapq
import sys

input = sys.stdin.readline


def _dijkstra(N: int, start_v: int, adj_list: list[list[tuple[int, int]]]):
    distances: list[int | float] = [float("inf")] * (N + 1)
    pq: list[tuple[int | float, int]] = [(0, start_v)]
    distances[start_v] = 0

    while pq:
        d, v = heapq.heappop(pq)
        if distances[v] != d:
            continue
        for adj_edge in adj_list[v]:
            next_v, w = adj_edge
            next_dist = w + distances[v]
            if next_dist < distances[next_v]:
                distances[next_v] = next_dist
                heapq.heappush(pq, (next_dist, next_v))

    return distances


def solution(N: int, adj_list: list[list[tuple[int, int]]], target_v: int):
    dist_table: list[list[int | float]] = []
    for i in range(N + 1):
        dist_table.append(_dijkstra(N, i, adj_list))

    return max(
        dist_table[v][target_v] + dist_table[target_v][v] for v in range(1, N + 1)
    )


def main():
    N, M, X = map(int, input().split())
    adj_list: list[list[tuple[int, int]]] = [[] for _ in range(N + 1)]
    for _ in range(M):
        start, end, weight = map(int, input().split())
        adj_list[start].append((end, weight))
    print(solution(N, adj_list, X))


if __name__ == "__main__":
    main()
