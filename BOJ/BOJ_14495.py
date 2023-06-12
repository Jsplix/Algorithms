import sys
input = sys.stdin.readline
# [BOJ] 14495 피보나치 비스무리한 수열 / DP
n = int(input())
similar_fibo = [1, 1, 1] + [0 for _ in range(115)]
for i in range(3, 117):
    similar_fibo[i] = similar_fibo[i-1] + similar_fibo[i-3]
print(similar_fibo[n-1])