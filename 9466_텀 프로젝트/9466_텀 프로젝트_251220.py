import sys

input = sys.stdin.readline
print = sys.stdout.write


def solution(n: int, selections: list[int]):
    visited = [False] * (n + 1)
    grouped = [False] * (n + 1)

    # stamp/visit_depth: "이번 탐색(run)"에서 방문 여부와 방문 순서
    stamp = [0] * (n + 1)
    visit_depth = [0] * (n + 1)

    run_id = 0
    team_count = 0

    for i in range(1, n + 1):
        if visited[i]:
            continue

        run_id += 1
        current_student = i
        depth = 0

        while True:
            visited[current_student] = True
            stamp[current_student] = run_id
            visit_depth[current_student] = depth
            depth += 1

            next_student = selections[current_student - 1]
            if not visited[next_student]:
                current_student = next_student
                continue

            if (not grouped[next_student]) and (stamp[next_student] == run_id):
                team_count += depth - visit_depth[next_student]
            break

        current_student = i
        while (stamp[current_student] == run_id) and (not grouped[current_student]):
            grouped[current_student] = True
            current_student = selections[current_student - 1]

    return n - team_count


if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        n = int(input())
        selections = list(map(int, input().split()))
        print(f"{solution(n, selections)}\n")
