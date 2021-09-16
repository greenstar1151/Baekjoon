import sys


N = int(input())
case_in = sys.stdin.read().rstrip()
cases = case_in.split('\n')


time_data = []
for c in cases:
    start, end = map(int, c.split())
    time_data.append( (start, end) )

time_data.sort(key=lambda x: (x[1], x[0]))

latest = -1
counter = 0
for t in time_data:
    if t[0] >= latest:
        latest = t[1]
        counter += 1
    
print(counter)
