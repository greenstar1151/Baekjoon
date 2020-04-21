current = {}
present = []

n = int(input())
for _ in range(n):
    employee, state = input().split()
    current[employee] = state

for employee, state in current.items():
    if state == 'enter':
        present.append(employee)

present.sort(reverse=True)


for s in present:
    print(s)
