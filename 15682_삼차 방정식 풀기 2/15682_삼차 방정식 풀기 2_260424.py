import sys
from decimal import Decimal, getcontext

input = sys.stdin.readline

getcontext().prec = 80

BOUND = Decimal("1000000")
ZERO = Decimal("1e-25")
ROOT_EPS = Decimal("1e-12")
BISECTION_STEPS = 200


def evaluate(a: Decimal, b: Decimal, c: Decimal, d: Decimal, x: Decimal) -> Decimal:
    return ((a * x + b) * x + c) * x + d


def is_zero(value: Decimal) -> bool:
    return -ZERO <= value <= ZERO


def derivative_roots(a: Decimal, b: Decimal, c: Decimal) -> list[Decimal]:
    discriminant = b * b - Decimal(3) * a * c

    if discriminant < 0:
        return []
    if is_zero(discriminant):
        return [-b / (Decimal(3) * a)]

    sqrt_discriminant = discriminant.sqrt()
    denominator = Decimal(3) * a
    first = (-b - sqrt_discriminant) / denominator
    second = (-b + sqrt_discriminant) / denominator
    return sorted([first, second])


def bisect_root(
    a: Decimal,
    b: Decimal,
    c: Decimal,
    d: Decimal,
    left: Decimal,
    right: Decimal,
) -> Decimal:
    left_value = evaluate(a, b, c, d, left)
    right_value = evaluate(a, b, c, d, right)

    if is_zero(left_value):
        return left
    if is_zero(right_value):
        return right

    for _ in range(BISECTION_STEPS):
        mid = (left + right) / 2
        mid_value = evaluate(a, b, c, d, mid)

        if is_zero(mid_value):
            return mid

        if (left_value < 0 < mid_value) or (left_value > 0 > mid_value):
            right = mid
            right_value = mid_value
        else:
            left = mid
            left_value = mid_value

    return (left + right) / 2


def unique_sorted_roots(roots: list[Decimal]) -> list[Decimal]:
    ordered: list[Decimal] = []

    for root in sorted(roots):
        if abs(root) < ROOT_EPS:
            root = Decimal(0)
        if not ordered or abs(root - ordered[-1]) > ROOT_EPS:
            ordered.append(root)

    return ordered


def solution(a: Decimal, b: Decimal, c: Decimal, d: Decimal) -> list[Decimal]:
    roots: list[Decimal] = []
    points = [-BOUND]

    for root in derivative_roots(a, b, c):
        if -BOUND < root < BOUND:
            points.append(root)

    points.append(BOUND)
    points.sort()

    values = [evaluate(a, b, c, d, point) for point in points]

    for point, value in zip(points, values):
        if is_zero(value):
            roots.append(point)

    for i in range(len(points) - 1):
        left_value = values[i]
        right_value = values[i + 1]

        if is_zero(left_value) or is_zero(right_value):
            continue
        if (left_value < 0 < right_value) or (left_value > 0 > right_value):
            roots.append(bisect_root(a, b, c, d, points[i], points[i + 1]))

    return unique_sorted_roots(roots)


if __name__ == "__main__":
    test_count = int(input())
    answers: list[str] = []

    for _ in range(test_count):
        a, b, c, d = map(Decimal, input().split())
        roots = solution(a, b, c, d)
        answers.append(" ".join(f"{root:.10f}" for root in roots) + "\n")

    sys.stdout.writelines(answers)
