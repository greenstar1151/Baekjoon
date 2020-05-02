import math


def menger(n: int):
    if n == 1:
        return [['*', '*', '*'],
                ['*', ' ', '*'],
                ['*', '*', '*']]
    else:
        p = menger(n - 1)
        l = len(p)
        sponge = [[' ' for _ in range(3*l)] for _ in range(3*l)]
        for c, i in enumerate(p):
            for r, j in enumerate(i):
                sponge[c][r] = j
                sponge[c][r + l] = j
                sponge[c][r + 2 * l] = j
                sponge[c + l][r] = j
                sponge[c + l][r + 2 * l] = j
                sponge[c + 2 * l][r] = j
                sponge[c + 2 * l][r + l] = j
                sponge[c + 2 * l][r + 2 * l] = j
        else:
            return sponge


n = round(math.log(int(input()), 3))


for l in menger(n):
    print('' .join(l))
