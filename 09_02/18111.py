import sys
input = sys.stdin.readline

n, m, b = map(int, input().split())#세로 가로 블록 수

grounds = list(list(map(int, input().split()))
               for i in range(n) )



t = 0

ans = [sys.maxsize, -1]#시간,높이


for h in range(0, 256 + 1):
    need_block = 0
    removed_block = 0
    

    for i1, v1 in enumerate(grounds):
        for i2, v2 in enumerate(v1):

            if v2 > h:#현재블록의 높이가 목표 높이보다 크다면 
                removed_block += grounds[i1][i2] - h
            
            else: #현재 블록의 높이가 목표 높이보다 낮다면
                need_block += h - grounds[i1][i2]
    
    if need_block <= removed_block + b:#필요 블럭이 가지게 되는 블럭보다 적다면, 즉 h에 도달하는것이 가능하다면
        t = removed_block * 2 + need_block * 1
        ans = [t, h] if (ans[0] > t or (ans[0] == t and ans[1] <= h)) else ans
                
    
print(*ans)




    

#어떻게 하지,, 하다가 https://aia1235.tistory.com/25 이 블로그를 보고 높이기준으로 하는 발상을 떠올림
