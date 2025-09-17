MODULO = 10**9 + 7


def solution(perf_multiples: tuple[int, ...]):
    prev_row_sum = 0
    total_sum = 0
    for m in perf_multiples[::-1]:
        prev_row_sum = m * (prev_row_sum + 1)
        prev_row_sum %= MODULO
        total_sum += prev_row_sum
        total_sum %= MODULO

    return total_sum


if __name__ == "__main__":
    N = int(input())
    M_i = tuple(map(int, input().split()))
    print(solution(M_i))
