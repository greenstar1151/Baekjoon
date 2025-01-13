import sys


def solution(tcs: list[str]):
    for tc in tcs:
        stack: list[str] = []
        for c in tc:
            if c == ".":
                break
            if c == "(" or c == "[":
                stack.append(c)
            elif c == ")":
                if stack and stack[-1] == "(":
                    stack.pop()
                else:
                    stack.append(c)
            elif c == "]":
                if stack and stack[-1] == "[":
                    stack.pop()
                else:
                    stack.append(c)
        if not stack:
            yield "yes\n"
        else:
            yield "no\n"


if __name__ == "__main__":
    tcs = sys.stdin.read().rstrip().split("\n")[:-1]
    sys.stdout.writelines(solution(tcs))
