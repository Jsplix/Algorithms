from collections import Counter
import sys
input = sys.stdin.readline
# [BOJ] 4158 CD / 자료 구조, 해시
while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    SG = {}
    chk = 0
    for _ in range(n):
        SG[int(input())] = 1
    for _ in range(m):
        if int(input()) in SG:
            chk += 1
    print(chk)