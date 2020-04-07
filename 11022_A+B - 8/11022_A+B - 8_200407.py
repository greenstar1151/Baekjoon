casecount = int(input())

for i in range(casecount):
    A, B = map(int, input().split())
    print("Case #{}: {} + {} = {}" .format(i + 1, A, B, A + B))
