import sys

input = sys.stdin.readline


def solution(seed: int):
    pool: set[int] = {seed}
    middle_square = seed
    while (middle_square := int(f"{middle_square**2:0>8}"[2:6])) not in pool:
        pool.add(middle_square)

    return len(pool)


if __name__ == "__main__":
    while True:
        seed = int(input())
        if seed == 0:
            break
        print(solution(seed))
