from sys import stdin
from collections import deque 
input = stdin.readline

n = int(input().rstrip())
INF = int(1e6)
m = int(input().rstrip())
broken = [False]*10
temp = list(map(int,input().rsplit()))
for i in temp:
    broken[i]=True 
result = abs(n-100)

for k in range(INF):
    num = str(k)
    for i in range(len(num)):
        if broken[int(num[i])] ==True:
            break 
        if i == len(num)-1:
            result = min(result, abs(n-k)+len(num)) #5457- 5000 = 457 + 4(숫자 누른 횟수) 
print(result)
