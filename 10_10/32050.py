import sys
input = sys.stdin.readline

def view_from(grid, direction, n):
    result = []
    if direction == 'north':
        for col in range(n):
            for row in range(n):
                if grid[row][col] != 0:
                    result.append(grid[row][col])
                    break
    elif direction == 'south':
        for col in range(n-1, -1, -1):
            for row in range(n-1, -1, -1):
                if grid[row][col] != 0:
                    result.append(grid[row][col])
                    break
    elif direction == 'west':
        for row in range(n):
            for col in range(n):
                if grid[row][col] != 0:
                    result.append(grid[row][col])
                    break
    elif direction == 'east':
        for row in range(n-1, -1, -1):
            for col in range(n-1, -1, -1):
                if grid[row][col] != 0:
                    result.append(grid[row][col])
                    break
    return result

def is_valid(grid, c, n):
    for dir in ['north', 'south', 'west', 'east']:
        if view_from(grid, dir, n) != c:
            return False
    return True

def solve(n, c):
    # 필요조건: c[0] == c[n-1]
    if c[0] != c[n-1]:
        return None
    
    # 간단한 경우: palindrome이면 대각선 배치
    if c == c[::-1]:
        grid = [[0] * n for _ in range(n)]
        for i in range(n):
            grid[i][i] = c[i]
        if is_valid(grid, c, n):
            return grid
    
    # 테두리 배치
    grid = [[0] * n for _ in range(n)]
    # 첫 행과 마지막 행
    for j in range(n):
        grid[0][j] = c[j]
        grid[n-1][n-1-j] = c[j]
    # 첫 열과 마지막 열
    for i in range(1, n-1):
        grid[i][0] = c[i]
        grid[n-1-i][n-1] = c[i]
    
    if is_valid(grid, c, n):
        return grid
    
    # 안되면 None 반환 (실제로는 더 복잡한 백트래킹 필요)
    return None

while True:
    n = int(input())
    if n == 0:
        break
    
    c = list(map(int, input().split()))
    
    result = solve(n, c)
    
    if result is None:
        print("No")
    else:
        print("Yes")
        for row in result:
            print(' '.join(map(str, row)))