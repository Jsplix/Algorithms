import sys
input = sys.stdin.readline
# [BOJ] 10211 Maximum Subarray / DP, 브루트포스, 누적 합
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    sm = [0 for _ in range(n)]

    sm[0] = arr[0]
    for i in range(1, n):
        sm[i] = max(sm[i-1]+arr[i], arr[i])
    
    print(max(sm))