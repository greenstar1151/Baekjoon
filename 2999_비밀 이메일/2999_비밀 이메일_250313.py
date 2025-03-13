def get_grid_size(n: int):
    pairs: list[tuple[int, int]] = []
    for i in range(1, n + 1):
        j = n / i
        if j.is_integer() and i <= j:
            pairs.append((i, int(j)))

    return sorted(pairs, reverse=True)[0]


def decipher(r: int, c: int, msg: str):
    for i in range(r):
        for j in range(c):
            yield msg[r * j + i]


def solution(msg: str):
    r, c = get_grid_size(len(msg))
    return "".join(decipher(r, c, msg))


if __name__ == "__main__":
    print(solution(input()))
