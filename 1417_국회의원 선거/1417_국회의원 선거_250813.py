import heapq
import sys


def solution(votes: list[int]):
    target = votes[0]
    vote_sim = [-v for v in votes[1:]]
    heapq.heapify(vote_sim)
    action_count = 0
    while vote_sim and True:
        current_votes = -heapq.heappop(vote_sim)
        if current_votes < target:
            break

        current_votes -= 1
        target += 1
        action_count += 1
        heapq.heappush(vote_sim, -current_votes)

    return action_count


if __name__ == "__main__":
    N, *votes = map(int, sys.stdin.read().strip().split("\n"))
    print(solution(votes))
