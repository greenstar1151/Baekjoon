prev_ord = float("inf")
k = 0
for c in input():
    if (c := ord(c)) <= prev_ord:
        k += 1
    prev_ord = c
print(k)
