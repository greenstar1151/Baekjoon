import sys

input = sys.stdin.readline


def solution(S: str, K: str):
    S = "".join(s for s in S if s.isalpha())

    return 1 if S.find(K) >= 0 else 0


if __name__ == "__main__":
    S = input().rstrip()
    K = input().rstrip()
    print(solution(S, K))
