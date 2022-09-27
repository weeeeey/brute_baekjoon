from sys import stdin 
dx = [0,0,-1,1]
dy = [-1,1,0,0]
input = stdin.readline

n,m = map(int,input().rsplit())
gr = [[] for i in range(n)]
for i in range(n):
    gr[i] = list(input().rstrip())

visited = [[False]*m for i in range(n)]
result = 0
sx = 0
sy = n-1

a_0 = int(''.join(gr[0]))    
s_0 = []
for i in range(m):
    temp = []
    for j in range(1,n):
        temp.append(gr[j][i])
    s_0.append(int(''.join(temp)))
for i in range(-1,-m-1,-1):
    a_0 = int(''.join(gr[0][:i]))
    print(a_0)