import sys
input = sys.stdin.readline
# [BOJ] 30008 준영이의 등급 / 수학, 구현, 사칙연산, 많은 조건 분기
n, k = map(int, input().split())
g = list(map(int, input().split()))
result = []

for i in range(k):
    if 0 <= (g[i]*100)//n <= 4: result.append(1)
    elif 4 < (g[i]*100)//n <= 11: result.append(2)
    elif 11 < (g[i]*100)//n <= 23: result.append(3)
    elif 23 < (g[i]*100)//n <= 40: result.append(4)
    elif 40 < (g[i]*100)//n <= 60: result.append(5)
    elif 60 < (g[i]*100)//n <= 77: result.append(6)
    elif 77 < (g[i]*100)//n <= 89: result.append(7)
    elif 89 < (g[i]*100)//n <= 96: result.append(8)
    elif 96 < (g[i]*100)//n <= 100: result.append(9)

print(*result)