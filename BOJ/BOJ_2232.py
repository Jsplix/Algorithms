import sys
input = sys.stdin.readline
# [BOJ] 2232 지뢰 / 그리디, 정렬
p = [0] + [int(input()) for _ in range(int(input()))] + [0]
for i in range(1, len(p)-1):
    if p[i-1] <= p[i] and p[i] >= p[i+1]:
        print(i)