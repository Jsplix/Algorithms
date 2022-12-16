import sys
input = sys.stdin.readline
# [BOJ] 16139 인간-컴퓨터 상호작용 / 누적 합
s = input().rstrip()
n = int(input())
alpha_arrange = [ [ 0 for _ in range(26) ] for _ in range(len(s)) ]
alpha_arrange[0][ord(s[0]) - ord('a')] += 1
for i in range(1, len(s)):
    alpha_arrange[i][ord(s[i]) - ord('a')] = 1
    for j in range(26):
        alpha_arrange[i][j] += alpha_arrange[i - 1][j] 

for _ in range(n):
    alphabet, l, r = input().split()
    l = int(l)
    r = int(r)
    if l > 0:
        ans = alpha_arrange[r][ord(alphabet) - ord('a')] - alpha_arrange[l - 1][ord(alphabet) - ord('a')]
    else:
        ans = alpha_arrange[r][ord(alphabet) - ord('a')]
    print(ans)