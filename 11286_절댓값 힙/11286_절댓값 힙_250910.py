import heapq
import sys
from typing import Generator


def solution(queries: list[int]):
    h: list[tuple[int, int]] = []

    for q in queries:
        if q == 0:
            if not h:
                yield 0
            else:
                yield heapq.heappop(h)[1]
        else:
            heapq.heappush(h, (abs(q), q))


def format_output(g: Generator[int, None, None]):
    for i in g:
        yield str(i)
        yield "\n"


if __name__ == "__main__":
    N, *queries = map(int, sys.stdin.read().strip().split("\n"))
    sys.stdout.writelines(format_output(solution(queries)))
