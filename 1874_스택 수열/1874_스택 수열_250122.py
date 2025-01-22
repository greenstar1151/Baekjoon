import sys


def solution(target_seq: list[int]):
    stack: list[int] = []
    num = 1
    for e in target_seq:
        while num <= e:
            stack.append(num)
            num += 1
            yield "+"
        if stack[-1] == e:
            stack.pop()
            yield "-"
    assert not stack


if __name__ == "__main__":
    n = int(input())
    target_sequence = list(map(int, sys.stdin.read().rstrip().split("\n")))
    try:
        sys.stdout.writelines("\n".join(solution(target_sequence)))
    except AssertionError:
        sys.stdout.write("NO")
    finally:
        sys.stdout.write("\n")
