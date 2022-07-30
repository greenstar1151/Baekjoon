N, k = map(int, input().split())
upper_bound = 0
exps = 0
while upper_bound < k:
    digits = exps + 1
    upper_bound += digits * 9 * 10 ** exps
    exps += 1

lower_bound = upper_bound - (exps) * 9 * 10 ** (exps - 1)
number_offset_from_lower, str_offset = divmod(k - lower_bound - 1, exps)
lower_bound_number = 10 ** (exps - 1) - 1
target_number = lower_bound_number + number_offset_from_lower + 1
if target_number > N:
    print(-1)
else:
    print(str(lower_bound_number + number_offset_from_lower + 1)[str_offset])
