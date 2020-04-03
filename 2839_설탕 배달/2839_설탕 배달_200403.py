N = int(input())

if N % 5 == 0:
    print(N // 5)
elif N % 5 == 1 and N >= 6:
    print((N // 5) + 1)
elif N % 5 == 2 and N >= 12:
    print((N // 5) + 2)
elif N % 5 == 3 and N >= 3:
    print((N // 5) + 1)
elif N % 5 == 4 and N >= 9:
    print((N // 5) + 2)
else:
    print(-1)