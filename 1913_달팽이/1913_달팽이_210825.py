import sys


def shell_N(x, y):
    x, y = abs(x), abs(y)
    shell = max(x, y)

    return shell#*2 + 1


N = int(input())
M = int(input())


coord_memo = [0, 0]
for i in range(N, 0, -1):
    for j in range(N):
        y, x = i - N//2 - 1, j - N//2
        s = shell_N(x, y)
        upper = (s*2 + 1)**2
        offset = s*2
        out = 1
        if x == -s and -s < y <= s:
            out = upper + (y - s)
        elif -s <= x < s and y == -s:
            out = upper - offset + (-x - s)
        elif x == s and -s <= y < s:
            out = upper - 2*offset + (-y - s)
        elif -s < x <= s and y == s:
            out = upper - 3*offset + (x - s)

        if out == M:
            coord_memo[0] = N - i + 1
            coord_memo[1] = j + 1
        
        sys.stdout.write(f'{out} ')
    sys.stdout.write('\n')
sys.stdout.write(f'{coord_memo[0]} {coord_memo[1]}')
