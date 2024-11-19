import sys
import heapq


def solution(N: int, schedules: list[tuple[int, ...]]):
    schedules.sort()
    pq = [schedules[0][1]]

    for s in schedules[1:]:
        if s[0] < pq[0]:  # 수업 시간이 겹치는 경우
            heapq.heappush(pq, s[1])
        else:
            # 해당 강의실에 수업 할당 가능
            # (겹치지 않는다면 아무 강의실에나 할당할 수 있으므로)
            heapq.heappop(pq)
            heapq.heappush(pq, s[1])

    return len(pq)


if __name__ == "__main__":
    N = int(sys.stdin.readline().rstrip())
    schedules = [
        tuple(map(int, schedule.split()))
        for schedule in sys.stdin.read().rstrip().split("\n")
    ]
    print(solution(N, schedules))
