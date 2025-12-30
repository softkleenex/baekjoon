# https://www.acmicpc.net/problem/28423

import sys
input = sys.stdin.readline



def Nc(N):
    def Na(N):
        N_str = (str(N))
        ans = 0
        
        for tempN in N_str:
            ans += int(tempN)
        
        return ans
    def Nb(N):
        N_str = (str(N))
        ans = 1
        
        for tempN in N_str:
            ans *= int(tempN)
        
        return ans
    
    return int(str(Na(N)) + str(Nb(N)))


l, r = map(int, input().split())
ans = 0

for i in range(l, r + 1):
    now = i
    for i2 in range(0, 100):
        tempnow = Nc(now)
        if now == tempnow:
            ans += 1
            break
        elif tempnow > 100000:
            ans -= 1
            break
        else:
            now = tempnow
    ans += 0
    
print(ans)