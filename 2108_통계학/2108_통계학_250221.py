import sys
from collections import Counter
from math import floor


def solution(N: int, numbers: list[int]):
    numbers.sort()
    minmax_diff = max(numbers) - min(numbers)
    average = sum(numbers) / N
    median = numbers[N // 2]
    counter = Counter(numbers).most_common()
    max_count = counter[0][1]
    modes = sorted([n[0] for n in counter if n[1] == max_count])
    mode = modes[0] if len(modes) < 2 else modes[1]

    return floor(average + 0.5), median, mode, minmax_diff


if __name__ == "__main__":
    N = int(input())
    numbers = list(map(int, sys.stdin.read().rstrip().split("\n")))
    print("\n".join(map(str, solution(N, numbers))))
