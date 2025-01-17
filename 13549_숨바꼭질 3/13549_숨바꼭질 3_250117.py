from collections import deque

MAX_SIZE = 1_000_001


def solution(N: int, K: int):
    time_taken = [-1] * MAX_SIZE  # -1 -> 아직 방문하지 않음
    q: deque[int] = deque()

    time_taken[N] = 0
    q.append(N)
    while q:
        pos = q.popleft()
        if pos == K:
            return time_taken[pos]
        if 0 <= pos * 2 < MAX_SIZE and time_taken[pos * 2] == -1:
            time_taken[pos * 2] = time_taken[pos]
            q.appendleft(pos * 2)  # 순간이동은 0초이므로 우선 탐색
        if 0 <= pos - 1 < MAX_SIZE and time_taken[pos - 1] == -1:
            time_taken[pos - 1] = time_taken[pos] + 1
            q.append(pos - 1)
        if 0 <= pos + 1 < MAX_SIZE and time_taken[pos + 1] == -1:
            time_taken[pos + 1] = time_taken[pos] + 1
            q.append(pos + 1)


if __name__ == "__main__":
    N, K = map(int, input().split())
    print(solution(N, K))
