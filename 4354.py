# https://www.acmicpc.net/problem/4354
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
        
    # result = []
    # i = 0
    
    # for j in range(len(all_string)):
    #     while i > 0 and pattern[i] != all_string[j]:
    #         i = table[i -1]
    #     if pattern[i] == all_string[j]:
    #         i += 1
    #         if i == len(pattern):
    #             result.append(j - i + 1)
    #             i = table[i - 1]
                
    return table

while(1):
    s = input().strip()
    len_s = len(s)
    ans = 1
    if s == '.':
        break
    else:
        ans = kmp(s, s)
        # print(ans)
        if len(s) % (len(s) - ans[-1]) == 0:
            print(len(s) // (len_s - ans[-1]))
        else:
            print(1)