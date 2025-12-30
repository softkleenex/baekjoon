# https://www.acmicpc.net/problem/9465

t = int(input())

pos = ((1, 0), (0, 1), (-1, 0), (0 , -1))

for i in range(t):
    n = int(input())
    st = [list(map(int, input().split())) for _ in range(2)]
    
    if n == 1:
        print(max(st[0][0], st[1][0]))
        continue
        
    dp = [[0] * n for _ in range(2)]
    dp[0][0] = st[0][0]
    dp[1][0] = st[1][0]
    dp[0][1] = dp[1][0] + st[0][1]
    dp[1][1] = dp[0][0] + st[1][1]

    for i in range(2, n):
        dp[0][i] = max(dp[1][i-1], dp[1][i-2], dp[0][i-2]) + st[0][i]
        dp[1][i] = max(dp[0][i-1], dp[0][i-2], dp[1][i-2]) + st[1][i]

    print(max(dp[0][n-1], dp[1][n-1]))

                    