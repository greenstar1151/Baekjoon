def d(n):
    return n + sum(map(int, str(n)))


s_num = [True] * 10001

for i in range(10001):
    if d(i) <= 10000:
        s_num[d(i)] = False

for i in range(10001):
    if s_num[i] == True:
        print(i)
