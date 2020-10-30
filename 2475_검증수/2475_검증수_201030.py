id_num = list(map(int, input().split(' ')))


print(sum([x**2 for x in id_num]) % 10)
