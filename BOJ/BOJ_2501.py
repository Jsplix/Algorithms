import sys
input = sys.stdin.readline
# [BOJ] 2501 약수 구하기 - 브루트 포스
n, k = map(int, input().split())
chk = []

for i in range(1, n + 1):
    if n % i == 0:
        chk.append(i)

if len(chk) >= k:
    print(chk[k - 1])
else:
    print(0)