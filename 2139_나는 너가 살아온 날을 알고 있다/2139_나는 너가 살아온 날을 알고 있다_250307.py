import sys

input = sys.stdin.readline

MONTH_DAYS = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def is_leap_year(year: int):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    return False


def get_day_count(day: int, month: int, year: int):
    days = 0
    days += sum(MONTH_DAYS[:month])
    days += day
    days += 1 if is_leap_year(year) and (month >= 3) else 0

    return days


def main():
    while True:
        d, m, y = map(int, input().split())
        if d == m == y == 0:
            return
        sys.stdout.write(f"{get_day_count(d, m, y)}\n")


if __name__ == "__main__":
    main()
