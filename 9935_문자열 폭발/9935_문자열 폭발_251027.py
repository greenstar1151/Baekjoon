def solution(string: str, target_str: str) -> str:
    target_len = len(target_str)
    stack: list[str] = []
    for c in string:
        stack.append(c)
        if c == target_str[-1]:
            if stack[-target_len:] == list(target_str):
                for _ in range(target_len):
                    stack.pop()

    if stack:
        return "".join(stack)

    return "FRULA"


if __name__ == "__main__":
    string = input()
    target_str = input()
    print(solution(string, target_str))
