on_train = 0
list_max = []

for i in range(4):
    get_off, get_on = map(int, input().split())
    on_train -= get_off
    list_max.append(on_train)
    on_train += get_on
    list_max.append(on_train)

print(max(list_max))