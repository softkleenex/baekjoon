import math
import sys
input = sys.stdin.readline


n = int(input())
list1 = list(map(int, input().split()))  
list_ans = sorted(list1[:])  


if list1 == list_ans:
    print("YES")
else:
   
    can_sort = True
    for i in range(n):
        if list1[i] != list_ans[i]:  
            if math.isqrt(list1[i] * list_ans[i]) ** 2 != list1[i] * list_ans[i]:
                can_sort = False
                break
    
    if can_sort:
        print("YES")
    else:
        print("NO")
