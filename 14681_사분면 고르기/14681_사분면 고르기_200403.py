x = int(input())
y = int(input())

if x * y < 0:
    if x > y:
        print("4")
    else:
        print("2")
else:
    if x > 0:
        print("1")
    else:
        print("3")
