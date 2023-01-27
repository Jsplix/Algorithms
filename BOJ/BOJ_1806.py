import sys
input = sys.stdin.readline
# [BOJ] 1806 부분합 / 누적 합, 투 포인터
# 이 문제의 N은 1~100,000까지임. 연속된 수열의 합을 구하는 가장 쉬운 방법은 이중 for문을 사용
# 하지만, 시간제한이 1초이므로 O(N^2)의 알고리즘은 사용하면 안됨. 따라서, 투 포인터를 사용해야함
n, s = map(int, input().split())
arr = list(map(int, input().split()))

chk, l, r = arr[0]+arr[1], 0, 1
arr_len = int(1e7)

if min(arr) == s or max(arr) == s: arr_len = 1
elif min(arr) > s or sum(arr) < s: arr_len = 0
else:
    while r <= n-1 and l <= n-1:
        if s <= chk:
            arr_len = min(arr_len, r-l+1)
            if s == chk:
                if r < n-1: 
                    r += 1
                    chk += arr[r]-arr[l]
                elif r == n-1:
                    chk -= arr[l]
                l += 1
            else:
                chk -= arr[l]
                l += 1
        elif s > chk:
            if r == n-1: break
            if r < n-1: 
                r += 1
                chk += arr[r]
print(arr_len)