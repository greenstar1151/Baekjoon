N, X = map(int, input().split())
numlist = list(map(int, input().split()))

for i in numlist:
    if i < X:
        print(i, end=" ")
    else:
        continue
