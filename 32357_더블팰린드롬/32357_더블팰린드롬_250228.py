def solution(strings: list[str]):
    count = len(list(filter(lambda s: s == s[::-1], strings)))
    return count * (count - 1)


if __name__ == "__main__":
    N, *strings = open(0).read().rstrip().split("\n")
    print(solution(strings))
