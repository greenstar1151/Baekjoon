import sys

X, Y = map(int, input().split())
N = int(input())
testcase_in = sys.stdin.read().rstrip()
testcase_in = testcase_in.split('\n')

price_list = [X / Y * 1000]
for testcase in testcase_in:
    X_i, Y_i = map(int, testcase.split())
    price_list.append(X_i / Y_i * 1000)

price_list.sort()
print(price_list[0])
