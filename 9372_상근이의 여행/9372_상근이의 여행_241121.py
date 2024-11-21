import sys

if __name__ == "__main__":
    T = int(sys.stdin.readline().rstrip())
    for _ in range(T):
        N, M = map(int, sys.stdin.readline().rstrip().split())
        # edges: list[list[int]] = [[] for _ in range(N + 1)]
        for _ in range(M):
            a, b = map(int, sys.stdin.readline().rstrip().split())
            # edges[a].append(b)
            # edges[b].append(a)
        # 가장 적은 "종류"의 비행기, (N개 정점인)연결 그래프의 최소 간선 개수는 N - 1개
        print(N - 1)
