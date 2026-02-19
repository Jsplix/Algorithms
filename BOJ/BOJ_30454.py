import sys
input = sys.stdin.readline
# [BOJ] 30454 얼룩말을 찾아라! / 구현, 문자열
N, L = map(int, input().split())
count = [0 for _ in range(501)]
mx = 0
for i in range(N):
    zebra = list(input().rstrip().split('0'))
    temp = zebra.count('')

    k = len(zebra) - temp
    mx = max(mx, k)
    count[k] += 1

print(mx, count[mx])