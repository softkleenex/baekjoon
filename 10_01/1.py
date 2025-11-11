# A번 - 디딤돌 장학금

l1 = list(map(int, input().split()))
n = int(input())
stu = []

for i in range(n):
    stu.append(list(map(float, input().split())))
    
m = 0

for v in stu:
    if v[1] >= 2.0 and v[2] >= 17:
         m += l1[int(v[0])]
         
print(m)
        