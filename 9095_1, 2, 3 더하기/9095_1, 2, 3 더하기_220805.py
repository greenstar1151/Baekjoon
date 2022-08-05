import sys 


T = int(input())
testcase_in = sys.stdin.read().rstrip()


dp_table = [0 for _ in range(12)]
dp_table[1:4] = [1, 2, 4]

for i in range(4, 12):
    dp_table[i] = dp_table[i-1] + dp_table[i-2] + dp_table[i-3]

for testcase in testcase_in.split('\n'):
    print(dp_table[int(testcase)])
