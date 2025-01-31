def solution(seq: list[int]):
    pos_counter = 1
    drop_counter = 0
    for a_k in seq:
        if a_k == pos_counter:
            pos_counter += 1
            continue
        drop_counter += 1
    return drop_counter


if __name__ == "__main__":
    N = int(input())
    A_k = list(map(int, input().split()))
    print(solution(A_k))
