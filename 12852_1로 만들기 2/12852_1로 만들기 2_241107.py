import sys


def solution(N: int):
    DP = [0 for _ in range(N + 1)]  # 1-based index
    path = [0 for _ in range(N + 1)]
    for i in range(2, N + 1):
        DP[i] = DP[i - 1] + 1
        path[i] = i - 1
        if i % 2 == 0 and (div2 := DP[i // 2] + 1) < DP[i]:
            DP[i] = div2
            path[i] = i // 2
        if i % 3 == 0 and (div3 := DP[i // 3] + 1) < DP[i]:
            DP[i] = div3
            path[i] = i // 3

    current_index = N
    route = [current_index]
    while current_index != 1:
        current_index = path[current_index]
        route.append(current_index)

    return DP[N], route


if __name__ == "__main__":
    N = int(sys.stdin.readline())
    min_count, route = solution(N)
    print(min_count)
    print(" ".join(map(str, route)))
