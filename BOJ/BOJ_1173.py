import sys
input = sys.stdin.readline
# [BOJ] 1173 운동 / 구현, 시뮬레이션
N, m, M, T, R = map(int, input().split())

mn, now = 0, 0
X = m
flag = False
while now < N:

    if X + T <= M:
        now += 1
        X += T
        flag = False
    else:
        if flag: mn = -1; break

        if X - R < m:
            X = m
            flag = True
        else:
            X -= R

    mn += 1

print(mn)