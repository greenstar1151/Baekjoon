import sys


n, m = map(int, sys.stdin.readline().split())
testcase_in = sys.stdin.read().rstrip()


row = [0 for _ in range(n)]
column = [0 for _ in range(m)]
testcase_in = testcase_in.split('\n')
testcase_in = [list(row.split()) for row in testcase_in]
for i in range(n):
    for j in range(m):
        nine_count = testcase_in[i][j].count('9')
        row[i] += nine_count
        column[j] += nine_count

if (row_max := max(row)) > (column_max := max(column)):
    row.remove(row_max)
    print(sum(row))
else:
    column.remove(column_max)
    print(sum(column))
