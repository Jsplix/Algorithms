import sys
input = sys.stdin.readline
# [BOJ] 14492 부울행렬의 부울곱 / 수학, 구현, 선형대수학
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
b = [list(map(int, input().split())) for _ in range(n)]
c = [[0 for _ in range(n)] for _ in range(n)]

cnt = 0
for k in range(n):
    for i in range(n):
        for j in range(n):
            if (a[k][j] and b[j][i]): cnt += 1; break

print(cnt)  