# N = int(input())
# N_list = map(int, input().split())
# M = int(input())
# M_list = map(int, input().split())


# space = {}
# for n in N_list:
#     space[n] = True

# for m in M_list:
#     exist = space.get(m, False)
#     if exist:
#         print(1)
#     else:
#         print(0)

N = int(input())
N_list = set(map(int, input().split()))
M = int(input())
M_list = map(int, input().split())


for m in M_list:
    if m in N_list:
        print(1)
    else:
        print(0)
