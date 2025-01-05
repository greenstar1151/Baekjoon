def solution(durations: list[int]):
    y, m = 0, 0
    for d in durations:
        y += ((d // 30) + 1) * 10
        m += ((d // 60) + 1) * 15
    if y == m:
        return f"Y M {y}"
    elif y > m:
        return f"M {m}"
    else:
        return f"Y {y}"


if __name__ == "__main__":
    N = int(input())
    durations = list(map(int, input().split()))
    print(solution(durations))
