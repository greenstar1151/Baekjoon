N, M = map(int, input().split())
notheard = set()
notseen = set()

for _ in range(N):
    notheard.add(input())

for _ in range(M):
    notseen.add(input())


notseenheard = notheard & notseen
out = list(notseenheard)
out.sort()


print(len(notseenheard))
for i in out:
    print(i)
