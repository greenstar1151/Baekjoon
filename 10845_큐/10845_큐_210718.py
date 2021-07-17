from collections import deque
import sys


N = int(input())
stdin = sys.stdin.read().rstrip()
queries = stdin.split('\n')


output = []
stack = deque()
def query_pop():
    try:
        output.append(f'{stack.popleft()}')
    except IndexError:
        output.append('-1')
def query_front():
    try:
        output.append(f'{stack[0]}')
    except IndexError:
        output.append('-1')
def query_back():
    try:
        output.append(f'{stack[-1]}')
    except IndexError:
        output.append('-1')

query_dict = {
    'pop': query_pop,
    'size': lambda: output.append(f'{len(stack)}'),
    'empty': lambda: output.append(f'{int(len(stack) == 0)}'),
    'front' : query_front,
    'back' : query_back
}
for q in queries:
    try:
        query_dict[q]()
    except KeyError:
        _, n = q.split()
        stack.append(int(n))

sys.stdout.write('\n'.join(output))
