import sys


testcase_in = sys.stdin.read().rstrip().split('\n')
N = int(testcase_in[0])
intervals = testcase_in[1:N+1]
queries = testcase_in[N+2:]

interval_sets = set()
lower_interval_sets = dict()
upper_interval_sets = dict()
for interval in intervals:
    lower, upper = map(int, interval.split())
    interval_sets.add((lower, upper))
    lower_interval_sets[lower] = max(lower_interval_sets.get(lower, float('-inf')), upper)
    upper_interval_sets[upper] = min(upper_interval_sets.get(upper, float('inf')), lower)
    
for query in queries:
    lower, upper = map(int, query.split())
    if (lower, upper) in interval_sets:
        print(1)
    elif lower_interval_sets.get(lower, float('-inf')) >= upper and upper_interval_sets.get(upper, float('inf')) <= lower:
        print(2)
    else:
        print(-1)
