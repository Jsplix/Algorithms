import sys
input = sys.stdin.readline
# [BOJ] 1083 소트 / 그리디, 정렬
n = int(input())
arr = list(map(int, input().split()))
s = int(input())

i = 0
while s != 0 and i < n:
    mxv = max(arr[i:i+s+1])
    mxi = arr.index(mxv)
    while i != mxi and s:
        arr[mxi-1], arr[mxi] = arr[mxi], arr[mxi-1]
        mxi -= 1
        s -= 1
    i += 1
    
print(*arr)