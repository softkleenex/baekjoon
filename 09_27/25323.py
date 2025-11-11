#https://www.acmicpc.net/status?from_mine=1&problem_id=25323&user_id=softkleenex

import math
import sys
input = sys.stdin.readline

        
        


n = int(input())
list1 = list(map(int, input().split()))  
list_ans = sorted(list1[:])  

if list1 == list_ans:
    print("YES")
else:
    for i in range(len(list1)):
        if list1[i] != list_ans[i]:
            if not math.isqrt(list1[i] * list_ans[i]) ** 2 == list1[i] * list_ans[i]:
                print("NO")
                exit()
    
    print("YES")