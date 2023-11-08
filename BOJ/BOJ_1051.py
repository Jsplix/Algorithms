import sys
input = sys.stdin.readline
# [BOJ] 1051 숫자 정사각형 / 구현, 브루트포스
n, m = map(int, input().split())
arr = [list(map(int, input().rstrip())) for _ in range(n)]
x = min(n, m)

sz = 1
for i in range(x):
    for j in range(n-i):
        for k in range(m-i):
            if arr[j][k] == arr[j][k+i] == arr[j+i][k] == arr[j+i][k+i]: 
                sz = max(sz, i+1)
print(sz**2)