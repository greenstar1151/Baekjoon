def solution(S: str, T: str):
    chars = list(T)
    target_len = len(S)
    while len(chars) > target_len:
        tail = chars[-1]
        if tail == "A":
            chars.pop()
        elif tail == "B":
            chars.pop()
            chars.reverse()

    if chars == list(S):
        return 1
    else:
        return 0


if __name__ == "__main__":
    S = input()
    T = input()
    print(solution(S, T))
