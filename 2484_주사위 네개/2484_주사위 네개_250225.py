import sys

input = sys.stdin.readline


def calculate_prize(dice: tuple[int, ...]):
    counts: dict[int, int] = {}
    for d in dice:
        counts[d] = counts.get(d, 0) + 1

    count_values = sorted(counts.items(), key=lambda x: (x[1], x[0]), reverse=True)

    match count_values:
        case [(value, 4)]:
            return 50000 + value * 5000
        case [(value, 3), *_]:
            return 10000 + value * 1000
        case [(value1, 2), (value2, 2)]:
            return 2000 + value1 * 500 + value2 * 500
        case [(value, 2), *_]:
            return 1000 + value * 100
        case _:
            return max(dice) * 100


def solution(dices: list[tuple[int, ...]]):
    max_prize = 0
    for dice in dices:
        prize = calculate_prize(dice)
        max_prize = max(max_prize, prize)

    return max_prize


if __name__ == "__main__":
    N = int(input())
    dices: list[tuple[int, ...]] = []
    for _ in range(N):
        dices.append(tuple(map(int, input().split())))

    print(solution(dices))
