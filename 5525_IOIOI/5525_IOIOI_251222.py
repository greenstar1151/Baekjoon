N = int(input())
M = int(input())
S = input()

state = "*"  # initial
P_n = 0
P_n_list: list[int] = []
for c in S:
    if state == "I":
        if c == "O":
            state = "O"
        else:  # c == "I"
            P_n_list.append(P_n)
            P_n = 0
            state = "I"
    elif state == "O":
        if c == "I":
            P_n += 1
            state = "I"
        else:  # c == "O"
            P_n_list.append(P_n)
            P_n = 0
            state = "*"
    elif c == "I":
        state = "I"
    else:  # c == "O"
        state = "*"


P_n_list.append(P_n)
print(sum(p - N + 1 for p in P_n_list if p >= N))
