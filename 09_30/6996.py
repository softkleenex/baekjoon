# https://www.acmicpc.net/problem/6996
from collections import Counter


t = int(input())

for _ in range(t):
    a, b = input().split()
    if Counter(a) == Counter(b):
        print(f"{a} & {b} are anagrams.")
    else:
        print(f"{a} & {b} are NOT anagrams.")