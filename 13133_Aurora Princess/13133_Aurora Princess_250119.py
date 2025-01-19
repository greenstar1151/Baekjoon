import sys

input = sys.stdin.readline


if __name__ == "__main__":
    N = int(input())
    people: list[tuple[int, int]] = []
    for _ in range(N):
        mom, dad, *_ = map(int, input().split())
        people.append((mom, dad))
    M = int(input())
    missing = set(map(int, input().split()))
    print(
        len(
            list(
                filter(
                    lambda x: missing.isdisjoint({x[0] + 1, x[1][0], x[1][1]})
                    and x[1][0] * x[1][1] != 0,
                    enumerate(people),
                )
            )
        )
    )
