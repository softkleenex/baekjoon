# https://www.acmicpc.net/problem/21866

l = list(map(int, input().split()))

l2 = [100, 100, 200, 200, 300, 300, 400 ,400, 500]

ans = -2#h -1 n 0 d 1

for i in range(len(l)):
    if l[i] > l2[i]:
        print('hacker')
        exit()
        
if sum(l) >= 100:
    print('draw')
else:
    print('none')