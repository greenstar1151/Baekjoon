import sys

input = sys.stdin.readline


def get_solve_history(log: list[tuple[int, int]]):
    for current in log:
        i, t = current
        for _ in range(t - 1):
            yield 0
        yield i


def solution(
    streak_freeze_count: int,
    period: int,
    problem_required_times: list[int],
) -> list[int]:
    times = [(t, i + 1) for i, t in enumerate(problem_required_times)]
    times.sort(key=lambda x: x[0])
    elapsed = 0
    freeze_left = streak_freeze_count
    logs: list[tuple[int, int]] = []
    for t, i in times:
        if elapsed + t > period:
            break
        elapsed += t
        freeze_left -= t - 1
        logs.append((i, t))

    if elapsed + freeze_left < period:
        return [-1]

    return list(get_solve_history(logs)) + [0] * (period - elapsed)


if __name__ == "__main__":
    N, M, K = map(int, input().split())
    times = list(map(int, input().split()))
    print(" ".join(map(str, solution(M, K, times))))
