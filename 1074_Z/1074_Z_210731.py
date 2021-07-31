N, r, c = map(int, input().split())


def found_pos(N, r, c):
    if N == 0:
        return 0
    l = 2 ** (N-1)
    return l ** 2 * (2*(r // l) + (c // l)) + found_pos(N-1, r % l, c % l)


print(found_pos(N, r, c))
