import sys
from collections import Counter
from functools import reduce
from operator import mul

input = sys.stdin.readline


def solution(counter: Counter[str]):
    num_cases = reduce(mul, (x + 1 for x in counter.values()), 1)
    num_cases -= 1  # 아무것도 선택하지 않은 경우 제외
    return num_cases


if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        n = int(input())
        counter: Counter[str] = Counter()
        for _ in range(n):
            _, category = input().split()
            counter.update((category,))
        print(solution(counter))
