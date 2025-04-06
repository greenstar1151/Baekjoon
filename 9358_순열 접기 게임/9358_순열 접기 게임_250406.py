import math
import sys

input = sys.stdin.readline


def solution(seq: list[int]):
    n = len(seq)
    while n > 2:
        next_seq: list[int] = []
        for i in range((n + 1) // 2):
            next_seq.append(seq[i] + seq[n - i - 1])
        n = math.ceil(n / 2)
        seq = next_seq

    if seq[0] > seq[1]:
        return "Alice"
    else:
        return "Bob"


if __name__ == "__main__":
    T = int(input())
    for t in range(1, T + 1):
        N = int(input())
        sequence = list(map(int, input().split()))
        print(f"Case #{t}: {solution(sequence)}")
