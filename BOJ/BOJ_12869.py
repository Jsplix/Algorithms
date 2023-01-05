from itertools import permutations
import sys
input = sys.stdin.readline
# [BOJ] 12869 뮤탈리스크 / DP
def solve(a, b, c, cnt):
    global ans
    if a <= 0 and b <= 0 and c <= 0:
        if ans > cnt:
            ans = cnt
            return
    
    if a <= 0: a = 0
    if b <= 0: b = 0
    if c <= 0: c = 0

    if dp[a][b][c] <= cnt and dp[a][b][c] != 0:
        return
    
    dp[a][b][c] = cnt

    for i in permutations(damage, 3):
        solve(a - i[0], b - i[1], c - i[2], cnt + 1)

damage = [9, 3, 1]

n = int(input())
hp = list(map(int, input().split()))
dp = [[[0 for _ in range(61)] for _ in range(61)] for _ in range(61)]
ans = int(1e9)

if n == 2:
    hp.append(0)
elif n == 1:
    hp.append(0)
    hp.append(0)
solve(hp[0], hp[1], hp[2], 0)
print(ans)