import sys

T = int(sys.stdin.readline())
case_in = sys.stdin.read().rstrip()
case_in = case_in.split('\n')

for N in case_in:
    N = int(N)
    if N % 9 == 0 or N % 3 == 2:
        print('TAK')
    else:
        print('NIE')
