import heapq
import sys

input = sys.stdin.readline


def solution(adj_list: list[list[tuple[int, int]]], start_v: int):
    distances: list[int | float] = [float("inf")] * len(adj_list)
    pq: list[tuple[int | float, int]] = [(0, start_v)]
    distances[start_v] = 0

    while pq:
        d, v = heapq.heappop(pq)
        if distances[v] != d:
            continue
        for adj_edge in adj_list[v]:
            next_v, w = adj_edge
            next_distance = w + distances[v]
            if next_distance < distances[next_v]:
                distances[next_v] = next_distance
                heapq.heappush(pq, (next_distance, next_v))

    for dist_from_start in distances[1:]:
        if dist_from_start == float("inf"):
            yield "INF"
        else:
            yield str(dist_from_start)
        yield "\n"


def main():
    V, E = map(int, input().split())
    K = int(input())
    adj_dict: list[dict[int, int]] = [{} for _ in range(V + 1)]
    for _ in range(E):
        u, v, w = map(int, input().split())
        if w_prev := adj_dict[u].get(v):
            if w < w_prev:
                adj_dict[u][v] = w
        else:
            adj_dict[u][v] = w
    adj_list = [list(edge.items()) for edge in adj_dict]
    sys.stdout.writelines(solution(adj_list, K))


if __name__ == "__main__":
    main()
