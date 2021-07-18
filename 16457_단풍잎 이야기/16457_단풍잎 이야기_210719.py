from itertools import combinations
import sys


n, m, k = map(int, input().split())
skills = range(1, 2*n + 1)
quests = []
for i in range(m):
    stdin_str = sys.stdin.readline().rstrip()
    quests.append(set(map(int, stdin_str.split())))

quest_count_list = []
for skillset in combinations(skills, n):
    quest_count = 0
    for q in quests:
        if q.issubset(set(skillset)):
            quest_count += 1
    quest_count_list.append(quest_count)

quest_count_list.sort(reverse=True)
print(quest_count_list[0])
