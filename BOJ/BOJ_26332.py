import sys
input = sys.stdin.readline
# [BOJ] 26332 Buying in Bulk / 수학, 사칙연산
for _ in range(int(input())):
    c, p = map(int, input().split())

    print(c, p)
    if c == 1: print(p)
    else: print(p + ((p-2) * (c-1)))