import sys

cases_in = sys.stdin.read().rstrip()
cases = tuple(cases_in.split('\n'))

for case in cases:
    l = len(case)
    if case == '0':
        break
    elif len(case) == 1:
        print('yes')
        continue
    elif case[:l//2] == case[l//2 + l%2:][::-1]:
        print('yes')
    else:
        print('no')
