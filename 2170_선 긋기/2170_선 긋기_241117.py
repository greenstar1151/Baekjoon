import sys


def solution(lines: list[tuple[int, ...]]):
    lines.sort(key=lambda x: (x[0], x[1]))
    furthest_start, furthest_end = lines[0]
    total_length = 0
    for line in lines[1:]:
        start, end = line
        # 선분이 겹치고 새 선분으로 현재 선분을 연장할 수 있는 경우
        if start <= furthest_end and end > furthest_end:
            furthest_end = end
        elif start > furthest_end:  # 선분이 겹치지 않는 경우
            # 이전 선분 길이 합산
            total_length += furthest_end - furthest_start
            # 새 선분 시작
            furthest_start = start
            furthest_end = end
    else:
        # 마지막 선분 길이 합산
        total_length += furthest_end - furthest_start
    return total_length


if __name__ == "__main__":
    N = int(sys.stdin.readline())
    lines = [
        tuple(map(int, line.split())) for line in sys.stdin.read().rstrip().split("\n")
    ]
    print(solution(lines))
