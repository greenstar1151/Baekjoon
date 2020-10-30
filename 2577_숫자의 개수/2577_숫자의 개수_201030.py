A = int(input())
B = int(input())
C = int(input())


numbers = [0] * 10

for n in str(A * B * C):
    numbers[ord(n) - 48] += 1


for i in numbers:
    print(i)
