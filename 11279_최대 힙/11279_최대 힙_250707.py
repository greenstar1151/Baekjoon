import sys
from heapq import heappop, heappush


def solution(ops: list[int]):
    pq: list[int] = []
    for op in ops:
        if op == 0:
            if len(pq) == 0:
                yield 0
                yield "\n"
                continue
            yield -heappop(pq)
            yield "\n"
            continue
        heappush(pq, -op)


if __name__ == "__main__":
    stdin = map(int, sys.stdin.read().rstrip().split("\n"))
    N, *ops = stdin
    sys.stdout.writelines(map(str, solution(ops)))
