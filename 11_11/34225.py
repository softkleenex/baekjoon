# https://www.acmicpc.net/problem/34225

import collections
from collections import deque
import itertools
import sys
input = sys.stdin.readline


    


n = int(input())
a_scores_ori = (list(map(int, input().split())))

for i in range(len(a_scores_ori)):
    a_scores_ori[i] = [a_scores_ori[i], i + 1]

a = sorted(a_scores_ori, reverse= True)

# print(a)

now = [[a[0][0] + a[0][0] + a[0][0], 0]]
# print(now[-1][0])




for i in range(1, len(a)):
        
        now.append(
            [now[-1][0] - a[i - 1][0] + a[i][0] + a[i][0], i]
            )

        
        
    



ans = max(now)

# print(ans[0])
# print(ans)

# print(a)
# print(ans[1])

print(ans[1] + 1)

for i in range(0, ans[1] + 1):
    print(a[i][1], end = ' ')