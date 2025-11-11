import sys
input = sys.stdin.readline

while True:
    n = int(input())
    if n == 0:
        break
    
    a, b, d = map(int, input().split())
    
    obstacles = set()
    for _ in range(n):
        x, y = map(int, input().split())
        obstacles.add((x, y))
    
    x, y = a, b
    dx, dy = 1, 0
    
    visited = {}
    moved = 0
    
    while moved < d:
        state = (x, y, dx, dy)
        
        if state in visited:
            cycle_start = visited[state]
            cycle_len = moved - cycle_start
            
            remaining = d - moved
            full_cycles = remaining // cycle_len
            
            moved += full_cycles * cycle_len
            
            if moved >= d:
                break
        else:
            visited[state] = moved
        
        nx, ny = x + dx, y + dy
        
        if (nx, ny) in obstacles:
            dx, dy = -dy, dx
        else:
            # 직선으로 갈 수 있으면 한번에 이동
            straight_dist = 0
            tx, ty = x, y
            
            while (tx + dx, ty + dy) not in obstacles and moved + straight_dist < d:
                tx += dx
                ty += dy
                straight_dist += 1
                
                if straight_dist > 200:  # 충분히 멀리 가면 끊기
                    break
            
            if straight_dist > 0:
                x, y = tx, ty
                moved += straight_dist
            else:
                x, y = nx, ny
                moved += 1
    
    print(x, y)