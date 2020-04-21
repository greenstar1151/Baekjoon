N = int(input())
cards_in = tuple(input().split())
M = int(input())
cards_query = tuple(input().split())
cards = {}
out = ''


for i in cards_in:
    if i in cards:
        cards[i] += 1
    else:
        cards[i] = 1

for k in cards_query:
    qtemp = cards.get(k)
    if qtemp == None:
        qtemp = 0
    else:
        pass
    out += (str(qtemp)+' ')


print(out)
