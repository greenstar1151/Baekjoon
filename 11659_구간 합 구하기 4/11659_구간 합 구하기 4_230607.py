import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
numbers_in = map(int, sys.stdin.readline().rstrip().split())
testcase_in = sys.stdin.read().rstrip().split('\n')

culmulative_sum = [0]
for number in numbers_in:
    culmulative_sum.append(culmulative_sum[-1] + number)

for data in testcase_in:
    i, j = map(int, data.split())
    print(culmulative_sum[j] - culmulative_sum[i-1])
