n = int(input())
numbers = list(map(int, input().split()))
dsum = 0

numbers.sort()
for i in range(n):
    dsum += numbers[i] * (2*(i+1) - 1)
    dsum -= numbers[-1 * i - 1] * (2*(i+1) - 1)

print(dsum)
