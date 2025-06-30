import sys
input = sys.stdin.readline
# [BOJ] 15732 도토리 숨기기 / 이분 탐색
def check(idx):
    ret = 0
    for s, e, c in rules:
        if idx < s: continue
        mn = min(idx, e)
        ret += (mn - s) // c + 1
    return ret

def binary_search(right, d):
    left = 0
    while left < right:
        mid = (left + right) // 2
        mid_check = check(mid)

        if mid_check < d:
            left = mid + 1
        else:
            right = mid 
    return left

n, k, d = map(int, input().split())
rules = [list(map(int, input().split())) for _ in range(k)]

print(binary_search(n, d))