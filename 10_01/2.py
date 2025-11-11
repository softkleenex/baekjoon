# B번 - 알파벳 점수 계산기

s = input()

pre = s[0]
pres = 1
ans = 1

for v in s[1:]:
    if v > pre:
        pres += 1
    else:
        pres = 1
    ans += pres
    pre = v
    
print(ans)