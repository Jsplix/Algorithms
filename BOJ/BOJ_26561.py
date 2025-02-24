import sys
input = sys.stdin.readline
# [BOJ] 26561 Population / 수학, 사칙연산
for _ in range(int(input())):
    p, t = map(int, input().split())
    p += -(t//7) + t//4
    print(p)