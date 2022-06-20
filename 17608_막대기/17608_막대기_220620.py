import sys


N = int(input())
testcase_in = sys.stdin.readlines()
sticks = map(int, testcase_in)

stack = []
for stick in sticks:
    while True:
        if len(stack) == 0:
            break
        if stack[-1] <= stick:
            stack.pop()
        else:
            break
    stack.append(stick)

print(len(stack))
