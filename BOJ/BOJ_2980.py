import sys
input = sys.stdin.readline
# [BOJ] 2980 도로와 신호등 / 수학, 구현, 시뮬레이션
n, l = map(int, input().split())
cnt, mv = 0, 0
for _ in range(n):
    d, r, g = map(int, input().split())
    cnt += (d-mv)
    mv = d
    if cnt % (r+g) <= r:
        cnt += (r-cnt%(r+g))
cnt += l-mv
print(cnt)