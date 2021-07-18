N = int(input())

target = 666
while N > 0:
    if '666' in str(target):
        N -= 1
        if N == 0:
            break
    target += 1

print(target)
