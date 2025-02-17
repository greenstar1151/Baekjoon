import sys

input = sys.stdin.readline


def solution(N: int, adj_list: list[list[tuple[int, int]]]):
    min_dist_table: list[list[int | float]] = [
        [float("inf")] * (N + 1) for _ in range(N + 1)
    ]
    for i in range(1, N + 1):
        min_dist_table[i][i] = 0
    for i, v_neighbors in enumerate(adj_list):
        for adj_v, weight in v_neighbors:
            min_dist_table[i][adj_v] = weight
    for stopover_v in range(1, N + 1):
        for start_v in range(1, N + 1):
            for end_v in range(1, N + 1):
                if (
                    stopover_path := min_dist_table[start_v][stopover_v]
                    + min_dist_table[stopover_v][end_v]
                ) < min_dist_table[start_v][end_v]:
                    min_dist_table[start_v][end_v] = stopover_path

    return min_dist_table


def format_table(min_dist_table: list[list[int | float]]):
    for row in min_dist_table[1:]:
        yield (
            " ".join(map(str, [d if d != float("inf") else 0 for d in row][1:])) + "\n"
        )


def main():
    n = int(input())
    m = int(input())
    adj_dict: list[dict[int, int]] = [{} for _ in range(n + 1)]
    for _ in range(m):
        start, end, weight = map(int, input().split())
        if old_weight := adj_dict[start].get(end):
            if weight < old_weight:
                adj_dict[start][end] = weight
        else:
            adj_dict[start][end] = weight
    adj_list = [list(edge.items()) for edge in adj_dict]
    sys.stdout.writelines(format_table(solution(n, adj_list)))


if __name__ == "__main__":
    main()
