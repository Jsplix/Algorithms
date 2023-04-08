import sys
input = sys.stdin.readline
# [BOJ] 10826 피보나치 수 4 / DP, 임의 정밀도, 큰 수 연산
n = int(input())
fibo = [0 for _ in range(10001)]
fibo[1], fibo[2] = 1, 1
for i in range(3, n + 1):
    fibo[i] = fibo[i-1] + fibo[i-2]
print(fibo[n])