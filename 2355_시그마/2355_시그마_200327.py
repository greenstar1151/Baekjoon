A, B = map(int, input().split())
lower = min(A, B)
upper = max(A, B)
sigmaL = 0
sigmaU = 0

def sigma(n):
    return((n * (n + 1)) // 2)


if lower > 0:
    sigmaL = sigma(lower)
elif lower < 0:
    sigmaL = sigma(abs(lower)) * -1
else:
    sigmaL = 0

if upper > 0:
    sigmaU = sigma(upper)
elif upper < 0:
    sigmaU = sigma(abs(upper)) * -1
else:
    sigmaU = 0

if upper < 0 and lower < 0:
    print(sigmaL - sigmaU + upper)
elif upper > 0 and lower > 0:
    print(sigmaU - sigmaL + lower)
else:
    print(sigmaU + sigmaL)