import sys


T = int(input())
case_in = sys.stdin.read().rstrip()
case_in = case_in.split('\n')


for testcase in case_in:
    V, E = map(int, testcase.split())
    F = E - V + 2
    print(F)
