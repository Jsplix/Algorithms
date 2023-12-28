import sys
input = sys.stdin.readline
# [BOJ] 16500 문자열 판별 / DP, 문자열
def solve(idx):
    global n
    if len(s) == idx:
        dp[-1] = 1
        return
    else:
        if dp[idx] != 1:
            dp[idx] = 1

            for i in range(n):
                if len(s[idx:]) >= len(words[i]):
                    for j in range(len(words[i])):
                        if s[idx+j] != words[i][j]:
                            break
                    else:
                        solve(idx+len(words[i]))

s = input().rstrip()
n = int(input())
words = [input().rstrip() for _ in range(n)]
dp = [0 for _ in range(len(s)+1)]

solve(0)
if dp[-1]: print(1)
else: print(0)