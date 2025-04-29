import sys


def get_quad_tree(img: list[list[str]], start_i: int, start_j: int, size: int) -> str:
    pixel = img[start_i][start_j]
    if size == 1:
        return pixel

    non_uniform = False
    for i in range(start_i, start_i + size):
        for j in range(start_j, start_j + size):
            if img[i][j] != pixel:
                non_uniform = True
                break
        if non_uniform:
            break
    else:
        return pixel

    next_size = size // 2
    upper_left = (start_i, start_j, next_size)
    upper_right = (start_i, start_j + next_size, next_size)
    lower_left = (start_i + next_size, start_j, next_size)
    lower_right = (start_i + next_size, start_j + next_size, next_size)
    return f"({get_quad_tree(img, *upper_left)}{get_quad_tree(img, *upper_right)}{get_quad_tree(img, *lower_left)}{get_quad_tree(img, *lower_right)})"


def solution(img: list[list[str]]):
    return get_quad_tree(img, 0, 0, len(img))


if __name__ == "__main__":
    N = int(input())
    img = [list(line) for line in sys.stdin.read().rstrip().split("\n")]
    print(solution(img))
