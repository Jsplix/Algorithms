import sys
input = sys.stdin.readline
# [BOJ] 13118 뉴턴과 사과 / 구현
p = list(map(int, input().split()))
x, y, r = map(int, input().split())

if x in p: print(p.index(x) + 1)
else: print(0)