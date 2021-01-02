N, M = map(int, input().split())
cards = list(map(int, input().split()))

card_sum = []
for i in range(len(cards) - 2):
    for j in range(i + 1, len(cards) - 1):
        for k in range(j + 1, len(cards)):
            card_sum.append(cards[i] + cards[j] + cards[k])
card_sum.sort()
for id, c in enumerate(card_sum):
    if c > M:
        if id == 0:
            print(card_sum[0])
        else:
            print(card_sum[id - 1])
        break
else:
    print(card_sum[-1])
