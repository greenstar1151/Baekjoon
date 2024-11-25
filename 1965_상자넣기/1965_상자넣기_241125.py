import sys

input = sys.stdin.readline


def solution(n: int, boxes: list[int]):
    # DP[i] -> i번째 상자까지 한 번에 넣을 수 있는 최대의 상자 개수
    DP = [0 for _ in range(n + 1)]
    DP[1] = 1

    for i in range(2, n + 1):
        candidates = [DP[j] for j in range(i) if boxes[j - 1] < boxes[i - 1]]
        DP[i] = max(candidates) + 1 if candidates else 1

    return max(DP)


if __name__ == "__main__":
    n = int(input())
    boxes = list(map(int, input().rstrip().split()))
    print(solution(n, boxes))
