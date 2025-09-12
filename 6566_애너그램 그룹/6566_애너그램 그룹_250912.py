import sys
from collections import Counter, defaultdict


class HashableCounter(Counter[str]):
    def __hash__(self) -> int:
        return hash(tuple((k, v) for k, v in sorted(self.items())))


def solution(words: list[str]):
    groups: defaultdict[HashableCounter, list[str]] = defaultdict(list)
    for word in words:
        groups[HashableCounter(word)].append(word)

    for group_words in groups.values():
        group_words.sort()

    return groups


def format_output(groups: defaultdict[HashableCounter, list[str]]):
    LIMIT = 5
    for i, group in enumerate(
        sorted(groups.items(), key=lambda x: (-len(x[1]), x[1][0]))
    ):
        if i >= LIMIT:
            break
        _, group_words = group
        yield f"Group of size {len(group_words)}: {' '.join(sorted(set(group_words)) + ['.'])}"
        yield "\n"


if __name__ == "__main__":
    words = sys.stdin.read().strip().split("\n")
    sys.stdout.writelines(format_output(solution(words)))
