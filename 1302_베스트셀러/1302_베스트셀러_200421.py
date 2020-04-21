N = int(input())
sale = {}
saletemp = 0

for _ in range(N):
    book = input()
    saletemp = sale.get(book)
    if saletemp == None:
        saletemp = 1
    else:
        saletemp += 1
    sale[book] = saletemp

sortedsale = sorted(sale.items(), key=lambda x: x[1], reverse=True)
topsale = []
k = sortedsale[0][1]

for i, j in sortedsale:
    if j < k:
        break
    k = j
    topsale.append(i)

topsale.sort()


print(topsale[0])
