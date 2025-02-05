from itertools import pairwise
from typing import Any, Iterable


def get_gunghap(num: list[int]):
    return [sum(pair) % 10 for pair in pairwise(num)]


def take_turns(seq1: Iterable[Any], seq2: Iterable[Any]):
    for s1, s2 in zip(seq1, seq2, strict=True):
        yield s1
        yield s2


def solution(num1: str, num2: str):
    num = list(take_turns(map(int, list(num1)), map(int, list(num2))))
    while len(num := get_gunghap(num)) > 2:
        pass

    return "".join(map(str, num))


if __name__ == "__main__":
    A = input()
    B = input()
    print(solution(A, B))
