import sys


def solution(scores: list[int]):
    scores.reverse()
    level_max_score = scores[0] - 1
    actions_count = 0
    for s in scores[1:]:
        if s > level_max_score:
            actions_count += s - level_max_score
        else:
            level_max_score = s
        level_max_score -= 1

    return actions_count


if __name__ == "__main__":
    N = int(sys.stdin.readline().rstrip())
    scores = list(map(int, sys.stdin.read().rstrip().split("\n")))
    print(solution(scores))
