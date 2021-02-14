import sys

N = int(input())
k = int(input())

lower = 1
upper = N
mid = (lower + upper) // 2
is_close = False

def count_under_mid(n, N):
    counter = 1
    for i in range(1, n):
        if i * N <= n ** 2:
            counter += 2 * (N - (i - 1)) - 1
        else:
            counter += 2 * ((n ** 2 // i) - (i - 1)) - 1
    return counter

if k == 1:
    print(1)
    sys.exit(0)
else:
    while True:
        under_count = count_under_mid(mid, N)
        if under_count < k:
            lower = mid
            mid = (lower + upper) // 2
        else:
            upper = mid
            mid = (lower + upper) // 2

        if under_count < k and lower == mid:
            break
    
#print(under_count, lower, mid, upper)

middle_numbers = []
for r in range(1, mid + 1):
    if r * N < mid ** 2:
        continue
    else:
        middle_numbers += list(range((mid ** 2 // r) * r + r, min(r * N + 1, (mid + 1) ** 2 + 1), r)) * 2
        middle_numbers += [(mid + 1) ** 2]

middle_numbers.sort()
#print(middle_numbers)
print(middle_numbers[k - under_count - 1])



'''
[1,  2,  3,  4,  5,  6,  7,  8,  9,  10]
[2,  4,  6,  8,  10, 12, 14, 16, 18, 20]
[3,  6,  9,  12, 15, 18, 21, 24, 27, 30]
[4,  8,  12, 16, 20, 24, 28, 32, 36, 40]
[5,  10, 15, 20, 25, 30, 35, 40, 45, 50]
[6,  12, 18, 24, 30, 36, 42, 48, 54, 60]
[7,  14, 21, 28, 35, 42, 49, 56, 63, 70]
[8,  16, 24, 32, 40, 48, 56, 64, 72, 80]
[9,  18, 27, 36, 45, 54, 63, 72, 81, 90]
[10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
'''
