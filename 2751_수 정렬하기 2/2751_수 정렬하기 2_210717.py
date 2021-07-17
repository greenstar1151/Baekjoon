import sys


N = int(input())
stdin = sys.stdin.read().rstrip()
nums = sorted(map(int, stdin.split('\n')))


print('\n'.join([str(n) for n in nums]))
