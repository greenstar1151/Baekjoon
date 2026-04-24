import math
import sys

input = sys.stdin.readline


def evaluate(a: int, b: int, c: int, d: int, x: int) -> int:
    return ((a * x + b) * x + c) * x + d


def find_integer_root(a: int, b: int, c: int, d: int) -> int:
    if d == 0:
        return 0

    abs_d = abs(d)
    limit = math.isqrt(abs_d)

    for divisor in range(1, limit + 1):
        if abs_d % divisor != 0:
            continue

        candidates = [divisor, -divisor]
        pair = abs_d // divisor
        if pair != divisor:
            candidates.extend([pair, -pair])

        for candidate in candidates:
            if evaluate(a, b, c, d, candidate) == 0:
                return candidate

    raise ValueError


def divide_by_root(a: int, b: int, c: int, d: int, root: int) -> tuple[int, int, int]:
    quad_a = a
    quad_b = b + quad_a * root
    quad_c = c + quad_b * root
    remainder = d + quad_c * root

    if remainder != 0:
        raise ValueError

    return quad_a, quad_b, quad_c


def quadratic_real_roots(a: int, b: int, c: int) -> list[float]:
    discriminant = b * b - 4 * a * c

    if discriminant < 0:
        return []
    if discriminant == 0:
        return [-b / (2 * a)]

    sqrt_discriminant = math.sqrt(float(discriminant))
    q = -0.5 * (float(b) + math.copysign(sqrt_discriminant, float(b)))
    first = q / float(a)
    second = float(c) / q
    return [first, second]


def unique_sorted_roots(roots: list[float]) -> list[float]:
    ordered: list[float] = []

    for root in sorted(roots):
        if abs(root) < 1e-12:
            root = 0.0
        if not ordered or abs(root - ordered[-1]) > 1e-7:
            ordered.append(root)

    return ordered


def solution(a: int, b: int, c: int, d: int) -> list[float]:
    integer_root = find_integer_root(a, b, c, d)
    quad_a, quad_b, quad_c = divide_by_root(a, b, c, d, integer_root)

    roots = [float(integer_root)]
    roots.extend(quadratic_real_roots(quad_a, quad_b, quad_c))
    return unique_sorted_roots(roots)


if __name__ == "__main__":
    test_count = int(input())
    answers: list[str] = []

    for _ in range(test_count):
        a, b, c, d = map(int, input().split())
        roots = solution(a, b, c, d)
        answers.append(" ".join(f"{root:.10f}" for root in roots) + "\n")

    sys.stdout.writelines(answers)
