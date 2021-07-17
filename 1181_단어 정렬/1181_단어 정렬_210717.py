import sys


N = int(input())
stdin = sys.stdin.read().rstrip()
words = stdin.split('\n')

words = sorted(set(words), key=lambda x: (len(x), x))
print('\n'.join(words))
