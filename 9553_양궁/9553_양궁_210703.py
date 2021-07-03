import math


# def is_overlapping(t1, t2, t): # t1, t2: 선분 꼭짓점의 각 | t가 t1, t2 사이에 있는가? | -pi < t* <= pi
#     t_lower = min(t1, t2)
#     t_upper = max(t1, t2)
#     if abs(t_upper - t_lower) >= math.pi:
#         t_lower += 2* math.pi
#         if t < 0: t += 2* math.pi

#     t_lower = min(t_lower, t_upper)
#     t_upper = max(t_lower, t_upper)
#     if (t_lower <= t <= t_upper):
#         return True
#     else:
#         return False

def is_overlapping(v1, v2, v): # v1, v2: 선분 꼭짓점의 좌표 | v가 v1, v2 사이에 있는가? 
    # (B.x)*(C.y) - (C.x)*(B.y) # A = (0,0)
    v1_v_ccw = v1[0]*v[1] - v[0]*v1[1]
    v2_v_ccw = v2[0]*v[1] - v[0]*v2[1]
    if ((v1_v_ccw < 0 and v2_v_ccw > 0)):
        return True
    else:
        return False

def theta_diff(t1, t2): # t1, t2 사이의 각(작은 쪽) 구하기 | t1, t2: atan2
    t_lower = min(t1, t2)
    t_upper = max(t1, t2)
    if abs(t_upper - t_lower) >= math.pi:
        t_lower += 2* math.pi

    return abs(t_upper - t_lower)


stdin = open(0).readlines()
stdin = [line.rstrip() for line in stdin]

T = int(stdin[0])
n_info = 1
for _ in range(T):
    N = int(stdin[n_info])
    points_theta_list = []
    points_theta_dict = {}
    lines_list = []
    for i in range(N):
        n_info += 1
        x1, y1, x2, y2 = map(int, stdin[n_info].split())
        points_theta_dict[(x1, y1)] = math.atan2(y1, x1)
        points_theta_dict[(x2, y2)] = math.atan2(y2, x2)
        # (theta, (x, y))
        points_theta_list.append( (points_theta_dict[(x1, y1)], (x1, y1)) )
        points_theta_list.append( (points_theta_dict[(x2, y2)], (x2, y2)) )
        lines_list.append( ((x1, y1), (x2, y2)) )
    n_info += 1

    points_theta_list = list(set(points_theta_list))
    points_theta_list.sort(key=lambda x: x[0])
    points_theta_list += [points_theta_list[0]]
    #print(points_theta_list)
    expected = 0
    # for i in range(len(points_theta_list) - 1):
    #     t1, p1 = points_theta_list[i]
    #     t2, p2 = points_theta_list[i+1]
    #     v = (p1[0]+p2[0], p1[1]+p2[1]) # sum of two vector
    #     if i == len(points_theta_list) - 2: v = (-v[0], -v[1])
    #     count = 0
    #     for line in lines_list:
    #         if is_overlapping(line[0], line[1], v):
    #             count += 1
    #     if t2 >= t1:
    #         theta = t2 - t1
    #     else:
    #         theta = t2 - t1 + 2*math.pi
    #     expected += count * theta
    #     print(count, v, (p1, p2), count * theta)
    # print(f'{round(expected/(2*math.pi), 5):.5f}')
    for l in lines_list:
        expected += theta_diff(points_theta_dict[l[0]], points_theta_dict[l[1]])
    print(f'{round(expected/(2*math.pi), 5):.5f}')
