from sys import stdin 
input = stdin.readline

n = int(input().rstrip())
result = set()

for K in range(n):
    sen = input().rsplit()
    if len(sen)==1: 
        if sen[0]=='all':
            result = set(i for i in range(1,21))
        else:
            result = set()
    else:
        NUM = int(sen[1])
        if sen[0]=='add':
            result.add(NUM)
        if sen[0]=='check':
            print(1 if NUM in result else 0)
        if sen[0]=='remove':
            if NUM in result:
                result.remove(NUM)
        if sen[0]=='toggle':
            if NUM in result:
                result.remove(NUM)
            else:
                result.add(NUM)
        