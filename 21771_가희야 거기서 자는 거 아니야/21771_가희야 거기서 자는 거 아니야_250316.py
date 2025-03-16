import sys
from collections import Counter

input = sys.stdin.readline


def solution(g_area: int, p_area: int, room: str):
    c = Counter(room.replace("\n", ""))
    if c["G"] == g_area and c["P"] == p_area:
        return 0
    elif c["G"] < g_area:
        return 0
    elif c["P"] < p_area:
        return 1


if __name__ == "__main__":
    R, C = map(int, input().split())
    R_g, C_g, R_p, C_p = map(int, input().split())
    room = sys.stdin.read().strip()
    print(solution(R_g * C_g, R_p * C_p, room))
