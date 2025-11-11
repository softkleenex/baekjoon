import sys

def get_mirror_pos(pos, size, reflect):
    if reflect % 2 == 0:
        return pos + reflect * size
    else:
        return (reflect + 1) * size - pos

def calc_time(sx, sy, tx, ty, a, b):
    ans = float('inf')
    
    for rx in range(-10, 11):
        for ry in range(-10, 11):
            mx = get_mirror_pos(tx, a, rx)
            my = get_mirror_pos(ty, b, ry)
            
            dx = mx - sx
            dy = my - sy
            
            if dx == dy and dx > 0:
                ans = min(ans, dx)
    
    return ans

def solve(a, b, cx, cy, balls):
    n = len(balls)
    answer = []
    
    for i in range(n):
        bx, by = balls[i]
        
        coin_t = calc_time(bx, by, cx, cy, a, b)
        if coin_t == float('inf'):
            continue
        
        ok = True
        
        # 다른 공이랑 먼저 부딪히는지
        for j in range(n):
            if i == j:
                continue
            ox, oy = balls[j]
            other_t = calc_time(bx, by, ox, oy, a, b)
            if other_t < coin_t:
                ok = False
                break
        
        if not ok:
            continue
        
        for hx, hy in [(0, 0), (a, 0), (a, b), (0, b)]:
            hole_t = calc_time(bx, by, hx, hy, a, b)
            if hole_t < coin_t:
                ok = False
                break
        
        if ok:
            answer.append(i + 1)
    
    return answer


while True:
    line = sys.stdin.readline().strip()
    if not line:
        continue
    
    parts = line.split()
    if len(parts) != 5:
        continue
    
    a, b, x, y, n = map(int, parts)
    if a == 0:
        break
    
    balls = []
    for _ in range(n):
        bx, by = map(int, sys.stdin.readline().split())
        balls.append((bx, by))
    
    result = solve(a, b, x, y, balls)
    
    if result:
        print(' '.join(map(str, result)))
    else:
        print('No')
