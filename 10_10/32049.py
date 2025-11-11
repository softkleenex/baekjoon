import sys
input = sys.stdin.readline

while True:
    n = int(input())
    if n == 0:
        break
    
    a, b, d = map(int, input().split())
    
    obs = set()
    for _ in range(n):
        x, y = map(int, input().split())
        obs.add((x, y))
    
    x, y = a, b
    dx, dy = 1, 0
    
    visited = {}
    moved = 0
    max_check = 100000
    
    while moved < d:
        if moved >= max_check:
            remain = d - moved
            x += dx * remain
            y += dy * remain
            break
        
        state = (x, y, dx, dy)
        
        if state in visited:
            cycle_start = visited[state]
            cycle_len = moved - cycle_start
            
            remain = d - moved
            full = remain // cycle_len
            left = remain % cycle_len
            
            # 남은 거리만큼 "실제 이동"
            steps_done = 0
            while steps_done < left:
                nx, ny = x + dx, y + dy
                if (nx, ny) in obs:
                    dx, dy = -dy, dx
                else:
                    x, y = nx, ny
                    steps_done += 1
            break
        
        visited[state] = moved
        
        nx, ny = x + dx, y + dy
        
        if (nx, ny) in obs:
            dx, dy = -dy, dx
        else:
            x, y = nx, ny
            moved += 1
    
    print(x, y)