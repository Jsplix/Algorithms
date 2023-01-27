import sys
input = sys.stdin.readline
# [BOJ] 1010 다리 놓기 / DP // -> 11051 이항 계수를 이용하여 계산
# 제한시간 0.5초이기 때문에 입력된 b(n), a(m) 값들 중 가장 큰 값으로 파스칼 삼각형 만들어줌
t = int(input())
n, r = [], []
for _ in range(t):
    a, b = map(int, input().split())
    n.append(b)
    r.append(a)

c = [ [0 for _ in range(max(n) + 1)] for _ in range(max(n) + 1) ]
for i in range(max(n) + 1): # c[n][r]
    c[i][0] = 1
    for j in range(i + 1):
        if j == i:
            c[i][j] = 1
        else:
            c[i][j] = c[i - 1][j - 1] + c[i - 1][j]
for i in range(t):
    print(c[n[i]][r[i]])