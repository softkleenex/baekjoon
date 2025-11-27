# https://www.acmicpc.net/problem/1260


import sys
input = sys.stdin.readline

n, m, v = map(int, input().split())

graph = [[] for i in range(0, n + 1)]

for i in range(m):
    s, t = map(int, input().split())
    graph[s].append(t)
    graph[t].append(s)
    
print(*graph, '\n')

def dfs(graph, start):
    n = len(graph)

    dp = [0] * n
    visited, finished = [False] * n, [False] * n

    stack = [start]
    while stack:
        start = stack[-1]

        # push unvisited children into stack
        if not visited[start]:
            visited[start] = True
            for child in graph[start]:
                if not visited[child]:
                    stack.append(child)
        else:
            stack.pop()

            # base case
            dp[start] += 1

            # update with finished children
            for child in graph[start]:
                if finished[child]:
                    dp[start] += dp[child]

            finished[start] = True

    return visited, dp



from collections import deque

def bfs(graph, start):
    n = len(graph)

    visited = [False] * n
    dist = [0] * n

    queue = deque([start])
    visited[start] = True

    while queue:
        node = queue.popleft()

        for child in graph[node]:
            if not visited[child]:
                visited[child] = True
                dist[child] = dist[node] + 1
                queue.append(child)

    return visited, dist



print(dfs(graph, v))
print(bfs(graph, v))