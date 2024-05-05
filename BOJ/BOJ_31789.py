import sys
input = sys.stdin.readline
# [BOJ] 31789 모험의 시작 / 구현
n = int(input())
x, s = map(int, input().split())
info = [ list(map(int, input().split())) for _ in range(n)]
flag = False
for c, p in info:
    if c <= x:
        if p > s: flag = True ; break

if flag: print("YES")
else: print("NO")