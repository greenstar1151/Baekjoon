from collections import deque


def solution(N: int, pop_targets: tuple[int, ...]):
    q = deque(range(1, N + 1))

    total_actions = 0
    for pop_target in pop_targets:
        left_actions, right_actions = 0, 0
        temp_q_left = q.copy()
        while temp_q_left[0] != pop_target:
            temp_q_left.appendleft(temp_q_left.pop())
            left_actions += 1
        temp_q_right = q.copy()
        while temp_q_right[0] != pop_target:
            temp_q_right.append(temp_q_right.popleft())
            right_actions += 1
        if left_actions > right_actions:
            temp_q_right.popleft()
            q = temp_q_right
        else:
            temp_q_left.popleft()
            q = temp_q_left

        total_actions += min(left_actions, right_actions)

    return total_actions


if __name__ == "__main__":
    N, M = map(int, input().split())
    pop_targets = tuple(map(int, input().split()))
    print(solution(N, pop_targets))
