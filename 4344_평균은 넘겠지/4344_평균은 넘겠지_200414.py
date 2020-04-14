C = int(input())

for _ in range(C):
    case = tuple(map(int, input().split()))
    casesum = sum(case[1:(case[0]+1)])
    avg = casesum / case[0]
    count = 0
    for i in case[1:]:
        if i > avg:
            count += 1
        else:
            continue
    print('%.3f%%' % ((count / (len(case) - 1)) * 100))
