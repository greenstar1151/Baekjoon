import sys
from typing import Any, Generator, Sequence


def list_combinations(seq: Sequence[Any], r: int):
    def combination(r: int, start: int, end: int) -> Generator[list[int], None, None]:
        if r == 1:
            for i in range(start, end):
                yield [i]
        else:
            for i in range(start, end):
                for next_combo in combination(r - 1, i + 1, end):
                    yield [i] + next_combo

    for selector in combination(r, 0, len(seq)):
        yield (seq[i] for i in selector)


def solution(N: int, M: int):
    for combo in list_combinations(range(1, N + 1), M):
        yield " ".join(map(str, combo))


if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().split())
    sys.stdout.write("\n".join(solution(N, M)) + "\n")


# # Solution using Built-in function
# from itertools import combinations

# N, M = map(int, input().split())
# print("\n".join(" ".join(map(str, c)) for c in combinations(range(1, N + 1), M)))
