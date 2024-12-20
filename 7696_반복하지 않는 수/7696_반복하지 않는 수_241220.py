import sys
from itertools import permutations, repeat, starmap
from operator import mul


def solution(n: int):
    number = (0,)
    counter = 0
    digits = 1
    permutation = permutations(range(10), digits)
    while counter < n:
        try:
            number = next(permutation)
            if number[0] == 0:
                continue
            counter += 1
        except StopIteration:
            digits += 1
            permutation = permutations(range(10), digits)
    return sum(starmap(mul, zip(map(pow, repeat(10), range(digits)), reversed(number))))


if __name__ == "__main__":
    while True:
        n = int(sys.stdin.readline())
        if n == 0:
            break
        print(solution(n))
