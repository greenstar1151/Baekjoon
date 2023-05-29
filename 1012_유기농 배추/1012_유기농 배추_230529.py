import sys

def visit(M, N, x, y):
    candidates = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
    return tuple(filter(lambda c: 0 <= c[0] < M and 0 <= c[1] < N, candidates))
    
testcase_in = sys.stdin.read().rstrip().split('\n')
T = int(testcase_in[0])
index_handle = 1
for _ in range(T):
    M, N, K = map(int, testcase_in[index_handle].split())
    visited = [[True for _ in range(M)] for _ in range(N)]
    index_handle += 1
    for data in testcase_in[index_handle:index_handle+K]:
        x, y = map(int, data.split())
        visited[y][x] = False
    cluster_count = 0
    for y in range(N):
        for x in range(M):
            if visited[y][x]:
                continue
            cluster_count += 1
            stack = [(x, y)]
            while len(stack) > 0:
                x_i, y_i = stack.pop()
                visited[y_i][x_i] = True
                for x_, y_ in visit(M, N, x_i, y_i):
                    if visited[y_][x_]:
                        continue
                    stack.append((x_, y_))
    print(cluster_count)
    index_handle += K

"""
처음에 왜 틀렸는가?

```
while len(stack) > 0:
    x, y = stack.pop()
    visited[y][x] = True
    for x_, y_ in visit(M, N, x, y):
        if visited[y_][x_]:
            continue
        stack.append((x_, y_))
```

x, y = stack.pop() 에서 x, y assign이 되고 다음 loop에서 변경된 x, y를 사용하게 되어서 문제가 발생

keyword:
Python은 declaration과 assignment 구분이 없다. 따라서 런타임에 유연하지만 위험하게 변경될 수 있음
    Declaration:
    int a;

    Assignment:
    a = 3;

    Declaration and assignment in one statement:
    int a = 3;

파이썬 scoping rule 동작 방식도 연관되어 있음
    for, while문은 scope를 새로 만들지 않기 때문에, global에 정의하면 변수들이 같은 스코프를 공유함 -> 모르고 덮어쓰기 쉬움 
"""