import sys
from collections import deque


def solution(A: int, B: int):
    q: deque[tuple[int, int]] = deque()
    q.append((A, 1))
    while q:
        next_num, depth = q.popleft()
        if next_num == B:
            return depth
        elif next_num > B:
            continue

        q.append((next_num * 2, depth + 1))
        q.append((10 * next_num + 1, depth + 1))

    return -1


if __name__ == "__main__":
    A, B = map(int, sys.stdin.readline().split())
    print(solution(A, B))
