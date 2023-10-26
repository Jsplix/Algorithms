import sys
input = sys.stdin.readline
# [BOJ] 30031 지폐 세기 / 수학, 구현, 사칙연산
d = {136: 1000, 142: 5000, 148: 10000, 154: 50000}
total = 0
for _ in range(int(input())):
    a, b = map(int, input().split())
    total += d[a]
print(total)