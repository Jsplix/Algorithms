import sys
input = sys.stdin.readline
# [BOJ] 1448 삼각형 만들기 / 수학, 그리디, 정렬
n = int(input())
lines = sorted(list(int(input()) for _ in range(n)))

idx = 0
while idx >= -(n-3):
    first, second, third = lines[idx-1], lines[idx-2], lines[idx-3]
    sm = first + second + third
    if first < second + third: print(sm) ; exit(0)
    idx -= 1
print(-1)