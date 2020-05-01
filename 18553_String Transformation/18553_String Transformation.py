'''
AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz
1121001101000100000000000000111111100000000000000000
'''
alphabet = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz'
holes = {'A':1,'a':1,'B':2,'b':1,'C':0,'c':0,'D':1,'d':1,'E':0,'e':1,'F':0,'f':0,'G':0,'g':1,'H':0,'h':0,'I':0,'i':0,'J':0,'j':0,'K':0,'k':0,'L':0,'l':0,'M':0,'m':0,'N':0,'n':0,'O':1,'o':1,'P':1,'p':1,'Q':1,'q':1,'R':1,'r':0,'S':0,'s':0,'T':0,'t':0,'U':0,'u':0,'V':0,'v':0,'W':0,'w':0,'X':0,'x':0,'Y':0,'y':0,'Z':0,'z':0}
distance = ((4,0,2),(3,0,1),(2,1,0),(1,0,51),(0,2,50),(0,1,49),(2,0,48),(1,0,47),(0,1,46),(1,0,45),(0,3,44),(0,2,43),(0,1,42),(1,0,41),(0,14,40),(0,13,39),(0,12,38),(0,11,37),(0,10,36),(0,9,35),(0,8,34),(0,7,33),(0,6,32),(0,5,31),(0,4,30),(0,3,29),(0,2,28),(0,1,27),(7,0,26),(6,0,25),(5,0,24),(4,0,23),(3,0,22),(2,0,21),(1,0,20),(0,17,19),(0,16,18),(0,15,17),(0,14,16),(0,13,15),(0,12,14),(0,11,13),(0,10,12),(0,9,11),(0,8,10),(0,7,9),(0,6,8),(0,5,7),(0,4,6),(0,3,5),(0,2,4),(0,1,3))
n, k = map(int, input().split())
string = input()

'''
if k > n * 2:
    print(-1)
'''
'''
# 입력 문자열의 각 문자 비용 출력 코드
tempdic = {}
for s in string:
    tempdic[s] = distance[alphabet.find(s)]
else:
    print(tempdic)
'''

'''
# 입력 문자열의 조정해야 하는 구멍 개수 출력 코드
holecount = 0
for s in string:
    holecount += holes.get(s)
else:
    deltahole = k - holecount
    print(deltahole)
'''
'''
zlEna

z+1:1, z+2:3
l+1:5, l+2:31
E+1:1, E+2:46
n+1:1, n+2:27
a-1:-3, a+1:1
'''