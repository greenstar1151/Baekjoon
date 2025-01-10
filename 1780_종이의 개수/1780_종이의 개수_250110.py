import sys

input = sys.stdin.readline


def count_paper(paper: list[tuple[int, ...]], x: int, y: int, n: int):
    # -1, 0, 1
    counts = [0, 0, 0]

    first = paper[x][y]
    is_same = all(
        paper[i][j] == first for i in range(x, x + n) for j in range(y, y + n)
    )

    if is_same:
        counts[first + 1] = 1
        return counts

    m = n // 3
    for i in range(3):
        for j in range(3):
            nx, ny = x + i * m, y + j * m
            sub_counts = count_paper(paper, nx, ny, m)
            for k in range(3):
                counts[k] += sub_counts[k]

    return counts


if __name__ == "__main__":
    n = int(input())
    paper = [tuple(map(int, input().split())) for _ in range(n)]

    print("\n".join(map(str, count_paper(paper, 0, 0, n))))
