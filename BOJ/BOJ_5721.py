import sys
input = sys.stdin.readline
# [BOJ] 5721 사탕 줍기 대회 / DP
def solution(lst: list):
    dp = [0 for _ in range(len(lst))]
    dp[0] = lst[0]

    if len(lst) >= 2: dp[1] = max(lst[0], lst[1])

    for i in range(2, len(lst)):
        dp[i] = max(dp[i-1], dp[i-2] + lst[i])
    
    return dp[-1]

while True:
    m, n = map(int, input().split())
    if m == 0 and n == 0: break
    boxes = [list(map(int, input().split())) for _ in range(m)]

    total = []
    for i in range(m):
        total.append(solution(boxes[i]))
    
    print(solution(total))