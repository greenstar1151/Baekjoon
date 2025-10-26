def count_digits_from_one(n: int) -> list[int]:
    if n < 0:
        return [0] * 10
    magnitude = 1
    digits_counts = [0] * 10
    while n // magnitude > 0:
        # cycle -> length of one complete 0->9 cycle for current magnitude
        cycle = magnitude * 10
        # How many complete cycles have occurred in 0->n at current magnitude?
        n_cycles = n // cycle
        for i in range(10):
            digits_counts[i] += n_cycles * magnitude
        # Get current phase within cycle and add count for digits 0->k-1
        phase = n % cycle
        for i in range(phase // magnitude):
            digits_counts[i] += magnitude
        # Add count for digit k
        digits_counts[phase // magnitude] += (
            phase - ((phase // magnitude) * magnitude) + 1
        )
        # Subtract leading zeros from previous magnitude
        digits_counts[0] -= magnitude

        magnitude *= 10

    return digits_counts


def solution(N: int):
    return " ".join(map(str, count_digits_from_one(N)))


if __name__ == "__main__":
    N = int(input())
    print(solution(N))
