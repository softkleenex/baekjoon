import sys
import bisect
input = sys.stdin.readline

q = int(input())
roots = []
deg = 0
coef = 1

for _ in range(q):
    cmd, *data = map(int, input().split())
    
    if cmd == 1:
        a, b = data
        if a != 0:
            r = -b / a
            bisect.insort(roots, r)
            deg += 1
            coef *= a
        else:
            coef *= b
    else:
        c = data[0]
        
        # c가 근인가 이진탐색
        pos = bisect.bisect_left(roots, c - 1e-9)
        is_root = pos < len(roots) and abs(roots[pos] - c) < 1e-9
        
        if is_root or coef == 0:
            print(0)
            continue
            
        # c보다 작은 근 개수 이진탐색
        cnt = bisect.bisect_left(roots, c)
        
        
        sign = 1
        if coef < 0:
            sign = -1
            
        
        if deg % 2 == 1:  # 홀수차
            if cnt % 2 == 0:  # 근 개수 짝 음수
                sign *= -1
        else:  # 짝수차
            if cnt % 2 == 1:  # 근 개수 홀 음수  
                sign *= -1
                
        print('+' if sign > 0 else '-')