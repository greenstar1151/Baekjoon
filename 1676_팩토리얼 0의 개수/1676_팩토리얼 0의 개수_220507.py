def factorize_5_or_2(n):
    count_5 = 0
    count_2 = 0
    while n % 5 == 0 or n % 2 == 0:
        if n % 5 == 0:
            count_5 += 1
            n = n // 5
        if n % 2 == 0:
            count_2 += 1
            n = n // 2
    return count_5, count_2


n = int(input())
count_5_all, count_2_all = 0, 0
for i in range(1, n + 1):
    count_5, count_2 = factorize_5_or_2(i)
    count_5_all += count_5
    count_2_all += count_2


print(min(count_5_all, count_2_all))
