import sys
input = sys.stdin.readline
# [BOJ] 34619 소대 배정 / 수학, 구현, 브루트포스, 사칙연산
a, b, n, k = map(int, input().split())
c = 0

for i in range(a):
    for j in range(b):
        for h in range(n):
            c += 1
            if c == k:
                print(i + 1, j + 1)
                exit(0)