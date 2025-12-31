# https://www.acmicpc.net/problem/1431


n = int(input())

seta = list()

for i in range(n):
    seta.append(input())
    
    
def key2(x):
    ans = 0
    for i in str(x):
        if i.isdigit():
            ans += int(i)
    
    return ans





seta.sort(key = lambda x : (len(x), key2(x), x))
    
    
seta.sort(key=lambda x: len(x))

print(*seta, sep = '\n')


