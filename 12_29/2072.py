# https://www.acmicpc.net/problem/2072


n = int(input())

table = [[0] * 19 for i in range(19)]


pos = ((1, 0), (1, 1), (0, 1), (1, -1))

for i in range(n):
    y, x = map(int, input().split())
    y -= 1
    x -= 1
    
    stone = 1 if i % 2 == 0 else 2
    
    table[y][x] = stone
    

    
    
    for i2 in pos:
        temp = 1
        ans = 1
        #정방향
        while 1:
            ny = y + i2[0] * temp
            nx = x + i2[1] * temp
            if 0 <= ny < 19 and 0 <= nx < 19 and table[ny][nx] == stone:
                ans += 1
                temp += 1
            else:
                break
        #역방향
        temp = 1
        while 1:
            ny = y - i2[0] * temp
            nx = x - i2[1] * temp
            
            if 0 <=  ny < 19 and 0 <= nx < 19 and table[ny][nx] == stone:
                ans += 1
                temp += 1
                
            else:
                break
        
        if ans == 5:
            print( i + 1)
            quit()

print(-1)