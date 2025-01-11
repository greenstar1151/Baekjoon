import sys
from typing import Generator


def list_nondecreasing_seq(N: int, M: int) -> Generator[tuple[int, ...], None, None]:
    path: list[int] = []

    def backtrack() -> Generator[tuple[int, ...], None, None]:
        if len(path) == M:
            yield tuple(path)
            return
        start = 1 if not path else path[-1]
        for i in range(start, N + 1):
            path.append(i)
            yield from backtrack()
            path.pop()

    yield from backtrack()


def solution(N: int, M: int):
    for seq in list_nondecreasing_seq(N, M):
        output = " ".join(map(str, seq))
        yield output


if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().split())
    sys.stdout.write("\n".join(solution(N, M)) + "\n")
