# https://www.acmicpc.net/problem/1487

n = int(input())

l = []

for i in range(n):
    a, b = map(int, input().split())
    l.append((a, b))
    
ls = sorted(l, key = lambda x : -x[0])

# print(ls)

m = 0
ans = 0

for i in range(len(ls)):
    
    tls = ls[0 : i + 1]
    tm = ls[i][0] #기준 금액
    temp_m = 0
    
    for i2 in range(len(tls)):
        if tm - tls[i2][1] >= 0:
            temp_m += tm - tls[i2][1]

    # print(tls, tm, temp_m)
    
    if temp_m > 0 and temp_m >= m:
        m = temp_m 
        ans = tm
    
print(ans)