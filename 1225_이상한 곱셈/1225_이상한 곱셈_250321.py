# from itertools import product, starmap
from operator import mul


# def solution(numbers: list[str]):
#     return sum(starmap(lambda x, y: int(x) * int(y), product(*numbers)))


def solution(numbers: list[str]):
    return mul(*map(lambda x: sum(map(int, x)), numbers))


if __name__ == "__main__":
    numbers = input().split()
    print(solution(numbers))
