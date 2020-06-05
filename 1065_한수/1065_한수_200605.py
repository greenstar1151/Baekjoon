N = int(input())

is_hansu = []
for i in range(100, 1000):
    numst = str(i)
    d = int(numst[1]) - int(numst[0])
    if int(numst[1]) + d >= 10 or int(numst[1]) + d < 0:
        continue
    elif int(numst[2]) == int(numst[1]) + d:
        is_hansu.append(i)


is_hansu_output = []
if N <= 99:
    print(N)
else:

    for h in is_hansu:
        if h <= N:
            is_hansu_output.append(h)
        else:
            pass
    else:
        print(99 + len(is_hansu_output))