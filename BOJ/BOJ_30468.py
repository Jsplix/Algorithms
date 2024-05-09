import sys
input = sys.stdin.readline
# [BOJ] 30468 호반우가 학교에 지각한 이유 1 / 수학, 구현, 사칙연산
s, d, i, l, n = map(int, input().split())
avg = (s + d + i + l) / 4

if avg >= n: print(0)
else: 
    sm = s + d + i + l
    print((4 * n) - sm)