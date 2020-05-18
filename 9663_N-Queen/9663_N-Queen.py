'''
import pprint


def 여왕님이나가신다길을비켜라(나여기있다:tuple, 판깔아봐라:list):
    상하 = 나여기있다[0]
    좌우 = 나여기있다[1]
    행차하실곳_예비타당성조사 = [(상하, 좌우)]
    행차하실곳 = []
    for 걸음 in range(1, len(판깔아봐라)):
        행차하실곳_예비타당성조사 += [(상하-걸음, 좌우-걸음), (상하-걸음, 좌우), (상하-걸음, 좌우+걸음), (상하, 좌우-걸음), (상하, 좌우+걸음), (상하+걸음, 좌우-걸음), (상하+걸음, 좌우), (상하+걸음, 좌우+걸음)]
    else:
        for (가, 나) in 행차하실곳_예비타당성조사:
            if 가 < 0 or 나 < 0:
                continue
            elif 가 >= len(판깔아봐라) or 나 >= len(판깔아봐라):
                continue
            else:
                행차하실곳 += [(가, 나)]
        for (가, 나) in 행차하실곳:
            판깔아봐라[가][나] = False
            

N = int(input())


체스판떼기 = [[True for _ in range(N)] for _ in range(N)]


for 가 in range(N):
    


# pprint.pprint(체스판떼기, width=100)
# 여왕님이나가신다길을비켜라((2, 2), 체스판떼기)
# pprint.pprint(체스판떼기, width=100)
'''


def placefinder(pos_list: list, N: int):
    if len(pos_list) == N:
        return 0
    next_row = [True for _ in range(N)]
    for index, value in enumerate(pos_list):
        next_row[value] = False
        for i in range(len(next_row)):
            if abs(len(pos_list) - index) == abs(i - value):
                next_row[i] = False
            else:
                continue
    else:
        print('placefinder', next_row)
        return next_row

casecount = 0
def queen_pos(pos_list, N):
    global casecount
    print('queen_pos', pos_list)
    if len(pos_list) >= N:
        casecount += 1
        print('casecount', casecount)
        return 0
    else:
        temp = placefinder(pos_list, N)
        if type(temp) == list:
            if not(True in temp):
                pos_list.pop()
                print('break')
                return 0
            for i, v in enumerate(temp):
                if not v:
                    continue
                else:
                    pos_list.append(i)
                    queen_pos(pos_list, N)
            else:
                return 0
        else:
            return 0
    


N = int(input())




for i in range(N):
    #print('mainloop',i)
    queen_pos([i], N)
else:
    print(casecount)