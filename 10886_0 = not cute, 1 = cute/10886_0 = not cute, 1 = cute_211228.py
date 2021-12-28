import sys


N = int(input())
case_in = sys.stdin.read().rstrip()
case_in = case_in.split('\n')


c = sum(map(int, case_in))
if c < N/2:
    print('Junhee is not cute!')
else:
    print('Junhee is cute!')
