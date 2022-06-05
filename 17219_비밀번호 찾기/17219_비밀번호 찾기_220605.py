import sys


N, M = map(int, input().split())
testcase_in = sys.stdin.readlines()
passwords = testcase_in[:N]
query = testcase_in[N:]
database = dict()

for data in passwords:
    url, pwd = data.split(' ')
    database[url.strip()] = pwd.strip()

output = []
for url in query:
    pwd = database.get(url.strip(), None)
    if pwd:
        output.append(pwd)

print('\n'.join(output))
