import sys
input = sys.stdin.readline
# [BOJ] 11501 주식 / 그리디
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    
    mx, val = 0, 0
    for i in range(n-1, -1, -1):
        if arr[i] > mx:
            mx = arr[i]
        else:
            val += mx-arr[i]
    print(val)