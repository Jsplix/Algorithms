import sys
input = sys.stdin.readline
# [BOJ] 4150 피보나치 수 / 임의 정밀도, 큰 수 연산
fibo = [0, 1, 1, 2, 3, 5]
n = int(input())
for i in range(6, n+1):
    fibo.append(fibo[i-1]+fibo[i-2])
print(fibo[n])