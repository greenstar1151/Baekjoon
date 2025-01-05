import sys


def get_distance(lane: str):
    lane = lane[1:-1][::-1]
    for i, c in enumerate(lane):
        if c != ".":
            return i, c
    return None, None


def solution(lanes: list[str]):
    teams: list[tuple[int, str]] = []
    for lane in lanes:
        distance, team = get_distance(lane)
        if team is None or distance is None:
            continue
        teams.append((distance, team))
    ranks = [-1] * 9
    rank, last_dist = 0, -1
    for distance, team in sorted(teams):
        if distance > last_dist:
            last_dist = distance
            rank += 1
        ranks[int(team) - 1] = rank
    return ranks


if __name__ == "__main__":
    R, C = map(int, sys.stdin.readline().split())
    lanes: list[str] = list(sys.stdin.read().rstrip().split("\n"))
    print("\n".join(map(str, solution(lanes))))
