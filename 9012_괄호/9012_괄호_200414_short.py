T=int(input())
for _ in range(T):
 c=input()
 while '()' in c:
  c=c.replace('()','')
 if len(c)!=0:
  print('NO')
 else:
  print('YES')