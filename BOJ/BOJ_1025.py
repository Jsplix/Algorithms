import sys
import math
input = sys.stdin.readline
# [BOJ] 1025 제곱수 찾기 / 브루트포스
n, m = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(n)]

answer = -1
for i in range(n):
    for j in range(m):
        for di in range(-n, n):
            for dj in range(-m, m):
                if di == 0 and dj == 0: continue
                chk = ''
                a, b = i, j

                while 0 <= a < n and 0 <= b < m:
                    chk += arr[a][b]
                    if int(math.sqrt(int(chk))) ** 2 == int(chk):
                        answer = max(answer, int(chk))
                    
                    a += di
                    b += dj

print(answer)