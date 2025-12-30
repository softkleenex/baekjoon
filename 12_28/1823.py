# https://www.acmicpc.net/problem/1823
import sys
sys.setrecursionlimit(2000)
input = sys.stdin.readline


n = int(input())
a = list()

for i in range(n):
    a.append(int(input()))
    
    
dp = list([-1] * n for i in range(n))

# print(*dp2, sep = '\n')

def max_rice(s,e):
    if s  == e:
        return n * a[s]
    
    if dp[s][e] == -1:
        k = n - (e - s) #n이, 리스트 크기가 4 라고 하자. s = 0, e = 3. k = 1이여야 한다
        
        if dp[s + 1] [e] == -1:
            left = k * a[s] + max_rice(s + 1, e)
        else:
            left = k * a[s] + dp[s+1][e]
        
        
        
        if dp[s] [e -1] == -1:
            right = k * a[e] + max_rice(s, e - 1)
        else:
            right = k * a[e] + dp[s][e - 1]
        
        
        dp[s][e] = max(left, right)
        
       
       
 
    return dp[s][e]
    
   


print(max_rice(0, n - 1))
    