# https://www.acmicpc.net/problem/1526


n = int(input())

while True:
    tn = set((' '.join(str(n))).split())
    # print(tn, set(['4','7']))
    if tn == set(['4','7']) or tn == set(['7']) or tn == set(['4']):
        print(n)
        break
    else:
        n -= 1
    
    if n < 0:
        break

