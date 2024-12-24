import sys
from math import ceil


def flip_sequence(sequence: list[int], start: int, end: int):
    for i in range(ceil(abs(start - end) / 2)):
        sequence[start + i], sequence[end - i] = sequence[end - i], sequence[start + i]


def solution(flip_ranges: list[tuple[int, ...]]):
    sequence = list(range(21))
    for flip_range in flip_ranges:
        start, end = flip_range
        flip_sequence(sequence, start, end)

    return sequence[1:]


if __name__ == "__main__":
    flip_ranges = [
        tuple(map(int, flip.split())) for flip in sys.stdin.read().rstrip().split("\n")
    ]
    print(" ".join(map(str, solution(flip_ranges))))
