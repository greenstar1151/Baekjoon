import sys


N = int(input())
stdin = sys.stdin.read().rstrip()
queries = stdin.split('\n')


output = []
stack = []
def query_pop():
    try:
        output.append(f'{stack.pop()}')
    except IndexError:
        output.append('-1')
def query_top():
    try:
        output.append(f'{stack[-1]}')
    except IndexError:
        output.append('-1')

query_dict = {
    'pop': query_pop,
    'size': lambda: output.append(f'{len(stack)}'),
    'empty': lambda: output.append(f'{int(len(stack) == 0)}'),
    'top' : query_top
}
for q in queries:
    try:
        query_dict[q]()
    except KeyError:
        _, n = q.split()
        stack.append(int(n))

sys.stdout.write('\n'.join(output))
