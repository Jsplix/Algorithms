import sys
input = sys.stdin.readline
# [BOJ] 24417 알고리즘 수업 - 피보나치 수 2 / 수학, DP
MOD = 10**9 + 7

n = int(input())
a, b = 1, 1
for i in range(n-2):
    b, a = (a + b) % MOD, b
print(b, n-2)