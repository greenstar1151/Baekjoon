import sys


def fizzbuzz(n: int):
    if n % 15 == 0:
        return "FizzBuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    else:
        return str(n)


if __name__ == "__main__":
    given_seq = sys.stdin.read().rstrip().split("\n")

    for i, s in enumerate(given_seq):
        if s.isdecimal():
            print(fizzbuzz(int(s) + (3 - i)))
            sys.exit(0)
