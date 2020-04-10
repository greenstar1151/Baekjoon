 
def cycle(n: int):
    return (n // 10 + n % 10) % 10 + ((n % 10) * 10)

N = int(input())
cycleN = cycle(N)
cyclecount = 1

while cycleN != N:
    cycleN = cycle(cycleN)
    cyclecount += 1
    #print(cycleN)

print(cyclecount)
