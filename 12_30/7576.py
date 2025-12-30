import sys
input = sys.stdin.readline
from collections import deque

m, n = map(int, input().split())

t = list(list(map(int, input().split())) for row in range(n))

# print(*t, sep = '\n')

maxday = 0
queue = deque()

for i in range(n):
    for j in range(m):
        if t[i][j] == 1:
            queue.append((i, j, 0))


pos = ((0, 1), (0, -1), (1, 0), (-1, 0))

if all(col != 0 for row in t for col in row):
    print(0)
    quit()

while queue:
    y, x, day = queue.popleft()
    
    for row, col in pos:
        ty, tx = y + row, x + col
        if (0 <= ty < n and 0 <= tx < m) and t[ty][tx] == 0:
            t[ty][tx] = 1 if t[ty][tx] == 0 else t[ty][tx]
            maxday = day + 1
            queue.append((ty, tx, maxday))
            
    
if any(col == 0 for row in t for col in row):
    print(-1)
    quit() 
else:  
    print(maxday)
    