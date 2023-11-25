import sys
input = sys.stdin.readline
# [BOJ] 2010 플러그 / 수학, 사칙연산
use = 1
for _ in range(int(input())):
    use += (int(input())-1)
print(use)