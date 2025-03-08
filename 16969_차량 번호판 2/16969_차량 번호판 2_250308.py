def solution(format_string: str):
    DIGIT_CASE = 10
    ALPHABET_CASE = 26
    total_cases = 1
    is_repeated = 0
    prev = "e"
    for char in format_string:
        if prev == char:
            is_repeated = 1
        else:
            is_repeated = 0
        if char == "c":
            total_cases = (total_cases * (ALPHABET_CASE - is_repeated)) % 1_000_000_009
        else:
            total_cases = (total_cases * (DIGIT_CASE - is_repeated)) % 1_000_000_009

        prev = char

    return total_cases


if __name__ == "__main__":
    format_string = input()
    print(solution(format_string))
