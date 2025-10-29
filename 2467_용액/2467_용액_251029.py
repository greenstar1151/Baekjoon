import sys

input = sys.stdin.readline


def solution(liquids: list[int]):
    l_handle, r_handle = 0, len(liquids) - 1
    l_liquid, r_liquid = liquids[l_handle], liquids[r_handle]

    while l_handle < r_handle:
        l_curr, r_curr = liquids[l_handle], liquids[r_handle]
        value = l_curr + r_curr
        if abs(value) < abs(l_liquid + r_liquid):
            l_liquid, r_liquid = l_curr, r_curr

        if value < 0:
            l_handle += 1
        else:
            r_handle -= 1

    return l_liquid, r_liquid


def format_output(result: tuple[int, int]):
    return " ".join(map(str, result))


if __name__ == "__main__":
    N = int(input())
    liquids = map(int, input().split())
    print(format_output(solution(list(liquids))))
