import sys
input = sys.stdin.readline
# [BOJ] 27965 N결수 / 수학, 정수론
n, k = input().split()
n_len = len(n)
n = int(n); k = int(k)
if k == 1:
    print(0)
    exit(0)

# N결수에 k를 modulo 연산한 결과 저장
dp = [0 for _ in range(n+1)] 
dp[1] = 1
for i in range(2, n+1):
    dp[i] = (dp[i-1] * (10**len(str(i))) + i) % k

print(dp[n])