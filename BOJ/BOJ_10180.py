import sys
input = sys.stdin.readline
# [BOJ] 10180 Ship Selection / 수학, 사칙연산
for _ in range(int(input())):
    n, d = map(int, input().split())
    count = 0
    for i in range(n):
        v, f, c = map(int, input().split())
        count += 1 if v * (f / c) >= d else 0
    print(count)