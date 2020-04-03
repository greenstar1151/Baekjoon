result = ["D", "C", "B", "A", "E"]
set_1 = list(map(int, input().split()))
set_2 = list(map(int, input().split()))
set_3 = list(map(int, input().split()))

print(result[sum(set_1)])
print(result[sum(set_2)])
print(result[sum(set_3)])
