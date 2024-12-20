import sys

input = sys.stdin.readline


def solution(c: int) -> list[int]:
    coin_types = [25, 10, 5, 1]
    amounts = [0] * 4
    handle = 0
    while c > 0:
        coin_type = coin_types[handle]
        coins, remainder = divmod(c, coin_type)
        amounts[handle] = coins
        c = remainder
        handle += 1

    return amounts


if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        print(" ".join(map(str, solution(int(input())))))
