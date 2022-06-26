import math


def solve(init_with: int, S: str):
    idx = 0
    current_num = S[:init_with]
    init_num = int(current_num)
    while True:
        if idx >= len(S):
            break   
        if current_num == S[idx:idx+len(current_num)]:
            idx += len(current_num)
            current_num = str(int(current_num) + 1)
        else:
            return False
    return init_num, int(current_num) - 1


S = input()


candidate = (math.inf, math.inf)
for i in range(1, 4):
    match solve(i, S):
        case init_num, current_num:
            if candidate[0] > init_num:
                candidate = (init_num, current_num)
        case False:
            pass

print(candidate[0], candidate[1])
