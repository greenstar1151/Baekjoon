import sys
from typing import Generator, Sequence, TypeVar

T = TypeVar("T")


def list_permutations(seq: Sequence[T], r: int) -> Generator[tuple[T, ...], None, None]:
    used = [False] * len(seq)
    path: list[T] = []

    def backtrack() -> Generator[tuple[T, ...], None, None]:
        if len(path) == r:
            yield tuple(path)
            return
        for i in range(len(seq)):
            if not used[i]:
                used[i] = True
                path.append(seq[i])
                yield from backtrack()
                path.pop()
                used[i] = False

    yield from backtrack()


def solution(numbers: Sequence[int], M: int):
    output_pool: set[str] = set()
    for combo in list_permutations(sorted(numbers), M):
        output = " ".join(map(str, combo))
        if output in output_pool:
            continue
        output_pool.add(output)
        yield output


if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().split())
    numbers = list(map(int, sys.stdin.readline().split()))
    sys.stdout.write("\n".join(solution(numbers, M)) + "\n")


# # Solution using Built-in function
# from itertools import permutations

# N, M = map(int, input().split())
# print(
#     "\n".join(
#         " ".join(map(str, c))
#         for c in sorted(set(permutations(map(int, input().split()), M)))
#     )
# )
