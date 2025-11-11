import sys
input = sys.stdin.readline

n = int(input())

l = list(map(int, input().split()))

k = int(input())

c = 0

#누적합
l2 = [0]

for i in range(len(l)):
    l2.append(l2[-1] + l[i])


for s in range(len(l)):
    for e in range(s, len(l)):
        if l2[e + 1] - l2[s] > k:
                c += len(l) - e
                break
            
                
print(c)