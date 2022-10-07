import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coin = []
for i in range(n):
    coin.append(int(input()))

start, end = 0, len(coin)
mid = (start + end) // 2
cnt = 0

while mid < end and k != 0:
    if start == mid:
        cnt += (k // coin[mid])
        k -= coin[mid] * (k // coin[mid])
        start = 0
    
    if k // coin[mid] > 0:
        start = mid
        mid = (start + end) // 2
    else:
        end = mid
        mid = (start + end) // 2

print(cnt)