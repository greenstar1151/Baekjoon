import sys


n, *a = map(int, input().split())
m = int(input())


a = set(a)
counter_pizza = 0
for _ in range(m):
    stdin_str = sys.stdin.readline()
    pizza = set(map(int, stdin_str.split()[1:]))
    if len(pizza & a) > 0:
        counter_pizza += 1
    
print(m - counter_pizza)
