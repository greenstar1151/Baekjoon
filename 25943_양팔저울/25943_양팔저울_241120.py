import sys

input = sys.stdin.readline


def solution(stones: tuple[int, ...]):
    left, right = stones[:2]
    for s in stones[2:]:
        if left <= right:
            left += s
        else:
            right += s

    diff = abs(left - right)
    counter = 0
    for weight in [100, 50, 20, 10, 5, 2, 1]:  # greedy
        while True:
            diff -= weight
            counter += 1
            if diff < 0:
                diff += weight
                counter -= 1
                break

    return counter


if __name__ == "__main__":
    n = int(input().rstrip())
    stones = tuple(map(int, input().rstrip().split()))
    print(solution(stones))
