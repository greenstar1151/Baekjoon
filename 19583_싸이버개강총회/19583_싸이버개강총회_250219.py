import sys
from collections import defaultdict
from itertools import chain

input = sys.stdin.readline


def timestamp_to_int(timestamp: str):
    h, m = map(int, timestamp.split(":"))
    return 60 * h + m


def solution(
    start: int, end: int, stream_end: int, chat_dict: defaultdict[int, list[str]]
):
    present_before = set(
        chain.from_iterable(
            name for _, name in filter(lambda x: start >= x[0], chat_dict.items())
        )
    )
    present_after = set(
        chain.from_iterable(
            name
            for _, name in filter(
                lambda x: end <= x[0] <= stream_end, chat_dict.items()
            )
        )
    )
    return len(present_before & present_after)


if __name__ == "__main__":
    S, E, Q = map(timestamp_to_int, input().split())
    chat_logs: list[tuple[int, str]] = []
    for log in sys.stdin.read().rstrip().split("\n"):
        timestamp, name = log.split()
        chat_logs.append((timestamp_to_int(timestamp), name))
    chat_logs.sort(key=lambda x: x[0])
    chat_dict: defaultdict[int, list[str]] = defaultdict(list)
    for t, name in chat_logs:
        chat_dict[t].append(name)
    print(solution(S, E, Q, chat_dict))
