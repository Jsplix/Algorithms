import sys
input = sys.stdin.readline
# [BOJ] 29720 그래서 님 푼 문제 수가? / 수학
n, m, k = map(int, input().split())
mn_solve, mx_solve = 0, 0

mn_solve = n-(m*k) if n-(m*k) >= 0 else 0
mx_solve = n-(m*k) + m-1
print(mn_solve, mx_solve)