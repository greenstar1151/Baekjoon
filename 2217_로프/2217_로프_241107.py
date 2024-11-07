import sys


def solution(N: int, ropes: list[int]):
    max_weight = 0
    ropes.sort()
    for i, r in enumerate(ropes):
        current_weight = (N - i) * r
        if current_weight > max_weight:
            max_weight = current_weight

    return max_weight


if __name__ == "__main__":
    N = int(sys.stdin.readline().rstrip())
    ropes = list(map(int, sys.stdin.read().rstrip().split("\n")))
    print(solution(N, ropes))
