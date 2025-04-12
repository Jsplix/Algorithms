import sys
input = sys.stdin.readline
# [BOJ] 18113 그르다 김가놈 / 이분 탐색, 매개 변수 탐색
n, k, m = map(int, input().split())
gimbap = []
for _ in range(n):
    l = int(input())
    if l <= k: continue
    elif l < 2*k: gimbap.append(l-k)
    else: gimbap.append(l-2*k)

p = -1
if gimbap:
    gimbap.sort()
    left, right = 1, gimbap[-1]
    while left <= right:
        mid = (left + right) // 2
        if not mid: break

        check = 0
        for i in range(len(gimbap)):
            check += gimbap[i] // mid
        
        if check < m:
            right = mid - 1
        else:
            left = mid + 1
            p = mid

print(p)