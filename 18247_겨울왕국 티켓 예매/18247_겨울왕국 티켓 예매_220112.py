import sys

T = int(input())
testcase_in = sys.stdin.read().rstrip()
testcase_in = testcase_in.split('\n')

for testcase in testcase_in:
    N, M = map(int, testcase.split())
    if M < 4 or N < 12:
        print(-1)
    else:
        print(11 * M + 4)
