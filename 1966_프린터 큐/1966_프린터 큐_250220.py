import sys
from collections import defaultdict, deque

input = sys.stdin.readline


def solution(target_index: int, q: list[int]):
    counter: defaultdict[int, int] = defaultdict(int)
    q_with_order: deque[tuple[int, int]] = deque()
    for item in q:
        q_with_order.append((item, counter[item]))
        counter[item] += 1
    target_item = q_with_order[target_index]
    pop_counter = 0
    while q_with_order:
        top = q_with_order.popleft()
        if len(list(filter(lambda x: x[0] > top[0], q_with_order))) > 0:
            q_with_order.append(top)
        else:
            pop_counter += 1
            if top == target_item:
                return pop_counter


if __name__ == "__main__":
    tc_count = int(input())
    for _ in range(tc_count):
        N, M = map(int, input().split())
        q = list(map(int, input().split()))
        print(solution(M, q))
