N = int(input())

for i in range(1, N):
    if N == i + sum(map(int, str(i))):
        print(i)
        break
else:
    print(0)
