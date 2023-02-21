import sys
input = sys.stdin.readline
MOD = 10**9 + 7
# [BOJ] 13171 A / 수학, 분할 정복을 이용한 거듭제곱
a = int(input())
x = int(input())

answer = 1
k = a
for b in bin(x)[2:][::-1]:
    if b == '1': answer = (answer * k) % MOD
    k = (k**2) % MOD
print(answer)