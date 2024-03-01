import sys
input = sys.stdin.readline
# [BOJ] 16493 최대 페이지 수 / DP, 브루트포스, 냅색(Knapsack), 배낭 문제, 백트래킹
def back(days, pages, idx):
    global n, m, mx
    if days > n: return
    else:
        mx = max(mx, pages)
        if days == n: return

    for i in range(idx, m):
        d, p = reading[i]
        back(days + d, pages + p, i + 1)


n, m = map(int, input().split())
reading = [tuple(map(int, input().split())) for _ in range(m)]
reading.sort(key= lambda x:(x[0], -x[1]))
mx = -1
back(0, 0, 0)
print(mx)