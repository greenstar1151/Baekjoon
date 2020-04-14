T = int(input())

for _ in range(T):
    case = input()
    while '()' in case:
        case = case.replace('()', '')
    if len(case) != 0:
        print('NO')
    elif len(case) == 0:
        print('YES')
