N = int(input())
scores = tuple(map(int, input().split()))


top = max(scores)
scores_new = []
for n in scores:
    scores_new.append(n / top * 100)


print(sum(scores_new) / len(scores_new))
