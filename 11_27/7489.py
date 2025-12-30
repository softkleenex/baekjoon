import math

t = int(input())

for i in range(t):
    n = int(input())
    ans = 1
    for i in range(1, n + 1):
        ans *= i
        if ans % 10 == 0:
            ans = ans //10
            
    while ans % 10 ==0:
        ans = ans // 10
    print(ans % 10)
    
    
    
    
