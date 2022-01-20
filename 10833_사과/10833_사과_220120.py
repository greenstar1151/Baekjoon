import sys


N = int(input())
testcase_in = sys.stdin.read().rstrip()
testcase_in = testcase_in.split('\n')

leftover_count = 0
for school in testcase_in:
    student_count, apple_count = map(int, school.split())
    leftover_count += apple_count % student_count

print(leftover_count)
