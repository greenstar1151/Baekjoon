import sys

def solution(n: int, containers: list[int]):
    move_count = 0
    total = sum(containers)
    avg_height = total // n
    over_height = sum(c - (avg_height + 1) for c in containers if c > avg_height + 1)
    under_height = sum(avg_height - c for c in containers if c <= avg_height)
    to_move = min(over_height, under_height)
    move_count += to_move
    over_height -= to_move
    under_height -= to_move
    move_count += over_height + under_height

    return move_count


if __name__ == "__main__":
    n, containers = sys.stdin.read().strip().split("\n")
    n, containers = int(n), list(map(int, containers.split()))
    print(solution(n, containers))
