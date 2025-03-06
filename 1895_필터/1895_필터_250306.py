import sys

input = sys.stdin.readline


def median_filter(
    img: list[list[int]], start_x: int, end_x: int, start_y: int, end_y: int
):
    pool: list[int] = []
    for i in range(start_x, end_x):
        for j in range(start_y, end_y):
            pool.append(img[i][j])
    pool.sort()
    return pool[len(pool) // 2]


def solution(img: list[list[int]], threshold: int):
    FILTER_SIZE = 3
    counter = 0
    for i in range(len(img) - FILTER_SIZE + 1):
        for j in range(len(img[0]) - FILTER_SIZE + 1):
            v = median_filter(img, i, i + FILTER_SIZE, j, j + FILTER_SIZE)
            if v >= threshold:
                counter += 1

    return counter


if __name__ == "__main__":
    R, C = map(int, input().split())
    img: list[list[int]] = []
    for _ in range(R):
        img.append(list(map(int, input().split())))
    T = int(input())
    print(solution(img, T))
