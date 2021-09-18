import sys


def index_match(connections: list) -> bool:
    stack = []
    for k in range(1, len(connections)):
        if connections[k] == 0:
            continue
        if len(stack) == 0:
            stack.append(connections[k])
            continue
        
        if stack[-1] == k:
            stack.pop()
        else:
            stack.append(connections[k])
    
    return len(stack) == 0


T = int(input())
case_in = sys.stdin.read().rstrip()
cases = case_in.split('\n')


for i in range(T):
    N = int(cases[2*i])
    paper = tuple(map(int, cases[2*i+1].split()))
    connections_L = [0 for _ in range(2001)]
    connections_R = [0 for _ in range(2001)]
    for j in range(len(paper) - 1):
        front, back = paper[j], paper[j+1]
        if j % 2 == 0:
            connections_L[front] = back
            connections_L[back] = front
        else:
            connections_R[front] = back
            connections_R[back] = front

    if index_match(connections_L) and index_match(connections_R):
        print('YES')
    else:
        print('NO')
