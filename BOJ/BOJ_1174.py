import sys
input = sys.stdin.readline
# [BOJ] 1174 줄어드는 수 / 브루트 포스, 백트래킹
def back(x, k, seq, now: list): # x자리 k로 시작하는 seq번째 수
    global chk, visited
    if len(now) == x:
        chk += 1
        if chk == seq: 
            print(''.join(map(str, now)))
            # exit(0)
        return
    
    for i in range(k, -1, -1):
        if not visited[i]:
            now.append(i)
            visited[i] = 1
            back(x, i-1, seq, now)
            visited[i] = 0
            now.pop()

n = int(input())

dp = [[0 for _ in range(10)] for _ in range(11)] # dp[i][j] - i자리, 앞의 수가 j로 시작
for i in range(0, 10): dp[1][i] = 1 # 한자리수는 모두 줄어드는 수

for i in range(2, 11):
    for j in range(i-1, 10):
        if j == i-1: dp[i][j] = 1
        else: dp[i][j] = dp[i][j-1] + dp[i-1][j-1]

cnt = 0
r, c = 1, 0
sm = 0

for i in range(1, 11):
    sm += sum(dp[i])

if n > sm: print(-1)
else:
    chk = 0
    visited = [0 for _ in range(10)]
    while cnt < n:
        if c == 10: r += 1 ; c = 0
        cnt += dp[r][c]
        c += 1

    back(r, c-1, cnt - n + 1, [])