import sys
input = sys.stdin.readline
# [BOJ] 13397 구간 나누기 2 / 이분 탐색, 매개변수 탐색
def check(val):
    global answer, n, m

    div = 1
    mn = 10007
    mx = 0

    for i in range(n):
        mn = min(mn, arr[i])
        mx = max(mx, arr[i])

        if mx - mn > val:
            div += 1
            mn = mx = arr[i]
    
    return m >= div

n, m = map(int, input().split())
arr = list(map(int, input().split()))

answer = 10007
left, right = 0, max(arr)
while left <= right:
    mid = (left + right) // 2

    if check(mid):
        right = mid - 1
        answer = min(mid, answer)
    else:
        left = mid + 1

print(answer)