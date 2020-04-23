import sys

K, L = map(int, input().split())
students_in = sys.stdin.read().rstrip()
students = tuple(students_in.split('\n'))


students_unique = set()
queue_reversed = []

for sid in reversed(students):
    if sid not in students_unique:
        queue_reversed.append(sid)
        students_unique.add(sid)

queue = tuple(reversed(queue_reversed))


for i in range(min(len(queue), K)):
    print(queue[i])
