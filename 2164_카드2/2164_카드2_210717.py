from collections import deque


N = int(input())

pile = deque(reversed(range(N)))
while len(pile) > 1:
    pile.pop()
    card = pile.pop()
    pile.appendleft(card)

print(pile[0] + 1)
