import sys


def ccw(x1: int, y1: int, x2: int, y2: int, x3: int, y3: int):
    return (x1 * y2 + x2 * y3 + x3 * y1) - (y1 * x2 + y2 * x3 + y3 * x1)


def get_area(x1: int, y1: int, x2: int, y2: int, x3: int, y3: int):
    return ccw(x1, y1, x2, y2, x3, y3) / 2


def solution(coords: list[tuple[int, ...]]):
    total_area = 0.0
    for i in range(1, len(coords) - 1):
        total_area += get_area(*coords[0], *coords[i], *coords[i + 1])

    return round(abs(total_area), 1)


if __name__ == "__main__":
    _, *coords = sys.stdin.read().strip().split("\n")
    coords = [tuple(map(int, coord.split())) for coord in coords]
    print(solution(coords))
