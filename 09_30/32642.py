# https://www.acmicpc.net/problem/32642

n = int(input())
rage = 0

l = list(map(int, input().split()))
ans = 0

for i in range(n):
    if l[i] == 1:
        rage += 1
    else:
        rage -= 1
        
    ans += rage
    
print(ans)