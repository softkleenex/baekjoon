from collections import deque


n_dq = deque(range(1, int(input()) + 1))

# print(dir(deque))

# print(n_dq)

while((not (len(n_dq) == 0)) and (not (len(n_dq) == 1))):
    print(deque.popleft(n_dq), end = ' ')
    n_dq.append(deque.popleft(n_dq))
    pass

print(n_dq[0])