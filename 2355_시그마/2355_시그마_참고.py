A,B = map(int, input().split())
X=max(A, B)
Y=min(A, B)
print((X+Y)*(X-Y+1)//2)
