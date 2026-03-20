def solution(S: str, T: str):
    def is_possible(t: str):
        if len(t) < 1:
            return False
        if S == t:
            return True
        if t[-1] == "A" and is_possible(t[:-1]):
            return True
        if t[0] == "B" and is_possible(t[::-1][:-1]):
            return True
        return False

    return 1 if is_possible(T) else 0


if __name__ == "__main__":
    S = input()
    T = input()
    print(solution(S, T))
