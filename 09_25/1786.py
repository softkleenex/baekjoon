# https://www.acmicpc.net/problem/1786
#refer
# https://bowbowbow.tistory.com/6
# https://yiyj1030.tistory.com/495

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
            
    #kmp
    result = []
    i = 0
    for j in range(len(all_string)):
        while i > 0 and pattern[i] != all_string[j]:
            i = table[i - 1]
        if pattern[i] == all_string[j]:
            i += 1
            if i == len(pattern):
                result.append(j - i + 1)
                i = table[i - 1]
                
    return result




t = input().rstrip()
p = input().rstrip()
# print(t)
# print(p)


ans = kmp(t, p)
print(len(ans))
for v in ans:
    print(v + 1)