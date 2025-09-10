# https://www.acmicpc.net/problem/34225

import sys
input = sys.stdin.readline


n = int(input())

a_list_origin = list(map(int, input().split()))
a_list = sorted(a_list_origin, key = lambda x : x)
a_list_index = [[a_list_origin[i - 1], i] for i in range(1, len(a_list_origin) + 1)]
a_list_index = sorted(a_list_index, key = lambda x : x[0])


ans = [a_list[-1], a_list[-1]]
ans_indices = [a_list_index[-1][1]]

if n == 1:
    print(1)
    print(*ans_indices)
    exit()


for i in range(len(a_list) - 2, -1, -1):
    if ans[-1] - a_list[i] < a_list[i]:
        ans.append(a_list[i])
        ans[0] += a_list[i]
        ans_indices.append(a_list_index[i][1])
    else:
        break
    
        
        
print(len(ans_indices))
print(*ans_indices, sep = ' ')
    