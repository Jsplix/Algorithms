import sys
input = sys.stdin.readline
# [BOJ] 1806 부분합 / 누적 합, 투 포인터
# 이 문제의 N은 1~100,000까지임. 연속된 수열의 합을 구하는 가장 쉬운 방법은 이중 for문을 사용
# 하지만, 시간제한이 1초이므로 O(N^2)의 알고리즘은 사용하면 안됨. 따라서, 투 포인터를 사용해야함

# -- 재채점 이후 틀림 >> elif min(arr) > s or sum(arr) < s: arr_len = 0 에서 수열의 최솟값이 s보다 크면
# -- 해당 원소 1개를 선택해서 길이 1인 부분합 수열을 만들 수 있음 따라서, 이 부분을 조정해야함.
# -- 이전 코드의 반례 (4 2 / 6 7 8 9) 였음. 따라서, 첫 번째 if에서 min(arr) > s 에서 min(arr) >= s 로 등호를 추가해줌.
n, s = map(int, input().split())
arr = list(map(int, input().split()))

chk, l, r = arr[0]+arr[1], 0, 1
arr_len = int(1e7)

if min(arr) >= s or max(arr) == s: arr_len = 1
elif sum(arr) < s: arr_len = 0
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