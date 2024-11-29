import sys
from collections import Counter

input = sys.stdin.readline


def solution(cards: tuple[int, ...], query: tuple[int, ...]):
    counter = Counter(cards)

    return (counter.get(q, 0) for q in query)


if __name__ == "__main__":
    N = int(input())
    cards = tuple(map(int, input().split()))
    M = int(input())
    query = tuple(map(int, input().split()))
    sys.stdout.write(" ".join(map(str, solution(cards, query))) + "\n")
