T = int(input())
for _ in range(T):
    case = input().split()
    R = int(case[0])
    S = case[1]
    print(''.join([x * R for x in S]))
