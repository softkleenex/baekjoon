# https://www.acmicpc.net/problem/16171


s = input()
k = list(' '.join(input()).split())


s2 = []
for i in range(len(s)):
    try:
        int(s[i])
        pass
    except:
        s2.append(s[i])
 

ans = 0

for i in range(len(s2)):
    try:        
        if s2[i : i + len(k) + 1] == k:
            ans = 1
    except:
        break
        
print(ans)