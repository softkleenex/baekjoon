# https://www.acmicpc.net/problem/21758

import sys
input = sys.stdin.readline

n = int(input())

honey = list(map(int, input().split()))


maxh = 0

nonreversed_h = honey.copy()


for i in range(1, n):
    nonreversed_h[i] += nonreversed_h[i-1]

#nonreversed_h[x] = 0~x까지의 누적합.

# print(honey)

# print(nonreversed_h)


# 벌 위치는 0, 1 or n-2, n-1 로 잡아보자.

#1. 벌통은 n-1. 첫번쨰 벌은 0. 두번쨰 벌은 가변
#2. 벌통은 0, 첫번째 벌은 n-1, 두번쨰 별은 가변
#3. 철번쨰 벌은 0 , 두번쨰 벌은 n-1, 벌통이 가변!!


for i in range(1, n):
    case1 = (nonreversed_h[n-1] - honey[i] - honey[0]) + (nonreversed_h[n-1] - nonreversed_h[i])#두번쨰 벌은 i + 1 ~ n-1까지의 누적합
    maxh = max(maxh, case1)
#     print(case1, maxh)

# print()
    
    
for i in range(1, n-1):
    case2 = (nonreversed_h[n-1] - honey[i]- honey[n - 1]) + (nonreversed_h[i-1])#두번쨰 벌은 0 ~ i -1낒;ㅇ,;
    maxh = max(maxh, case2)
    # print(case2, maxh)
 
 
for i in range(1, n-1):
    case3 = nonreversed_h[n-1] - honey[0] - honey[n-1] + honey[i]
    #1 ~ i까지 누적합 + i ~ n-2까지 누적합. > 사실
    maxh = max(maxh, case3)
    # print(case2, maxh)
    

    
print(maxh)