import sys
import heapq


def solution(n: int, m: int, cards: list[int]):
    heapq.heapify(cards)
    for _ in range(m):
        new_card = heapq.heappop(cards) + heapq.heappop(cards)
        heapq.heappush(cards, new_card)
        heapq.heappush(cards, new_card)

    return sum(cards)


if __name__ == "__main__":
    n, m = map(int, sys.stdin.readline().rstrip().split())
    cards = list(map(int, sys.stdin.readline().rstrip().split()))
    print(solution(n, m, cards))
