# https://www.acmicpc.net/problem/1787

import sys
input = sys.stdin.readline

def kmp(all_string, pattern):  
    table = [0 for _ in range(len(pattern))]
    i = 0
    for j in range(1, len(pattern)):
        while i > 0 and pattern[i] != pattern[j]:
            i = table[i - 1]
        if pattern[i] == pattern[j]:
            i += 1
            table[j] = i
            
    return table


n = int(input())
s = input().strip()

ans = kmp(s,s)


result = 0

dp = [-1] * n
for i in range(len(ans)):
    if  dp[i] == -1:
        dp[i] = ans[i]
    
    r = dp[i]
    
    while 1:
        if r - 1 >= 0 and ans[r -1] > 0:
            if dp[r - 1] == -1:
                dp[r - 1] = ans[r - 1]
                
            r = dp[r - 1]
                
        else:
            break
    if r > 0:
        result += (i + 1 - r)
    
print(result)