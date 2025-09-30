q = int(input())

for _ in range(q):
    a, m = map(int, input().split())
    x = int((a *m * 1056) /(60 * 10000))
    print(x)