import sys
input = sys.stdin.readline
# [BOJ] 1990 소수인팰린드롬 / 수학, 정수론, 소수 판정, 에라토스테네스의 체
MX = int(1e8)
r = int(MX**0.5)+1

def Eratosthenes():
    global a, b
    for i in range(2, int(b**0.5)+1):
        if not num[i]: continue
        for j in range(i*i, b+1, i):
            num[j] = 0

a, b = map(int, input().split())
b = int(1e7) if b >= int(1e7) else b
num = [0, 0] + [1 for _ in range(b)]
Eratosthenes()

cnt = 0
for i in range(a, b+1):
    if num[i]:
        chk = str(i)
        if chk == chk[::-1]:
            print(i)
print(-1)