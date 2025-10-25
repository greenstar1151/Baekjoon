def count_bin_ones_from_zero(n: int) -> int:
    if n < 0:
        return 0
    magnitude = 1
    one_count = 0
    while n // magnitude > 0:
        cycle = magnitude * 2
        n_cycles = n // cycle
        one_count += n_cycles * magnitude
        is_phase_over_half = True if (n % cycle) >= magnitude else False
        if is_phase_over_half:
            one_count += (n % cycle) - magnitude + 1
        magnitude *= 2

    return one_count


def solution(A: int, B: int):
    return count_bin_ones_from_zero(B) - count_bin_ones_from_zero(A - 1)


if __name__ == "__main__":
    A, B = map(int, input().split())
    print(solution(A, B))
