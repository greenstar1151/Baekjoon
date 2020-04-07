# 빠른 소수 판별 함수 by https://53perc.tistory.com/entry/파이썬-소수-판별하기
def is_prime(n: int) -> bool: 
    if n == 1:                # 원래는 if n < 2:        이지만, 2153번 조건에서 1도 소수로 취급한다.
        return False          #            return False
    if n in (2, 3):
        return True
    if n % 2 is 0 or n % 3 is 0:
        return False
    if n < 9:
        return True
    k, l = 5, n**0.5
    while k <= l:
        if n % k is 0 or n % (k+2) is 0:
            return False
        k += 6
    return True

alphabet_index = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z")

word_in = input()
strsum = 0

for s in word_in:
    strsum += alphabet_index.index(s) + 1

print(strsum)

if is_prime(strsum) == True:
    print("It is a prime word.")
elif is_prime(strsum) == False:
    print("It is not a prime word.")
