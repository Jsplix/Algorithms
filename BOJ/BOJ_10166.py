import sys
from math import gcd
input = sys.stdin.readline
# [BOJ] 10166 관중석 / 수학, 정수론, 유클리드 호제법
d1, d2 = map(int, input().split())

answer = 0
check = [[0 for _ in range(2007)] for __ in range(2007)]
for i in range(d1, d2+1):
    for j in range(1, i+1):
        g = gcd(i, j)

        a, b = i // g, j // g
        
        # 좌석 설치가 되지 않은 곳
        if not check[a][b]: 
            check[a][b] = 1

for row in check:
    answer += sum(row)

print(answer)