import sys


T = int(input())
case_in = sys.stdin.read().rstrip()
cases = list(map(int, case_in.split('\n')))

mine_list = []
prev = cases[0]
cases = cases + [cases[-1] - 1]
flip = True
for i in range(1, len(cases)):
    if prev < cases[i]:
        flip = True
    elif prev == cases[i]:
        if flip:
            mine_list.append(i)
        flip = True
    else:
        if flip:
            mine_list.append(i)
            flip = False
    prev = cases[i]

print('\n'.join(map(str, mine_list)))
