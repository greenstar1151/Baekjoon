import sys

input = sys.stdin.readline


def solution(S: str) -> int:
    chunks_count = [0, 0]

    prev_char = S[0]
    chunks_count[int(prev_char)] += 1
    for s in S[1:]:
        if s != prev_char:
            chunks_count[int(s)] += 1
        prev_char = s
    return min(chunks_count)


if __name__ == "__main__":
    S = input().rstrip()
    print(solution(S))
