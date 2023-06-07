import sys
from itertools import product


white_count = int
blue_count = int


def count_color_sqaure(
    paper_data: list[list[int]], x_start: int, y_start: int, size: int
) -> tuple[white_count, blue_count]:
    if size == 1:
        if paper_data[y_start][x_start] == 0:
            return 1, 0
        else:
            return 0, 1
    else:
        counter = 0
        for i in range(size):
            for j in range(size):
                counter += paper_data[y_start + i][x_start + j]
        if counter == 0:
            return 1, 0
        elif counter == size**2:
            return 0, 1
        else:
            half_size = size // 2
            white_count, blue_count = 0, 0
            for x_add, y_add in product([0, half_size], [0, half_size]):
                w, b = count_color_sqaure(
                    paper_data, x_start + x_add, y_start + y_add, half_size
                )
                white_count += w
                blue_count += b
            return white_count, blue_count


N = int(sys.stdin.readline().rstrip())
paper_data_in = sys.stdin.read().rstrip().split("\n")
paper_data = [list(map(int, line.split())) for line in paper_data_in]

white_count, blue_count = count_color_sqaure(paper_data, 0, 0, N)
print(white_count)
print(blue_count)
