# https://www.acmicpc.net/problem/27930
import collections


s = input()
t1= ['Y', 'O', 'N', 'S', 'E', 'I']
t2 = ['K', 'O', 'R', 'E', 'A']



tt1 = 0
tt2 = 0
for i2, v2 in enumerate(s):
    if v2 == t1[tt1]:
        tt1 += 1
    if v2 == t2[tt2]:
        tt2 += 1
    if tt1 == 6:
        print("YONSEI")
        break
    if tt2 == 5:
        print("KOREA")
        break