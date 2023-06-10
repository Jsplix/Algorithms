import sys
input = sys.stdin.readline
# [BOJ] 15624 피보나치 수 7 / 수학, DP
MOD = 1000000007
n = int(input())

fibo = [0, 1]
for i in range(2, n+1):
    fibo.append((fibo[i-1] + fibo[i-2]) % MOD)

print(fibo[n])