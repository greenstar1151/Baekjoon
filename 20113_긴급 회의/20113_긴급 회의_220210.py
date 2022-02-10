from collections import Counter

N = int(input())
votes = Counter(filter(lambda x: x != 0, map(int, input().split())))
count = sorted(votes.items(), key=lambda x: x[1], reverse=True)
if count[0][1] in [x[1] for x in count[1:]]:
    print('skipped')
else:
    print(count[0][0])
