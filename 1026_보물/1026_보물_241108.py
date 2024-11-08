import sys


def solution(A: list[int], B: list[int]):
    A.sort()
    B.sort(reverse=True)

    return sum(a * b for a, b in zip(A, B))


if __name__ == "__main__":
    N = int(sys.stdin.readline())
    A = list(map(int, sys.stdin.readline().split()))
    B = list(map(int, sys.stdin.readline().split()))
    print(solution(A, B))
