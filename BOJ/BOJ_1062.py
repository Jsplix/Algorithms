import sys
input = sys.stdin.readline
# [BOJ] 1062 가르침 / 브루트 포스, 백트래킹
n, k = map(int, input().split())
words = [ set(input().rstrip()) for _ in range(n) ]
std = ['a', 'c', 'i', 'n', 't']
chk = [ 0 for _ in range(26) ]
ans = 0

for c in std:
    chk[ord(c) - ord('a')] = 1

def dfs(idx, cnt):
    global ans
    if cnt == k - 5:
        real_cnt = 0
        for word in words:
            mark = False
            for c in word:
                if not chk[ord(c) - ord('a')]:
                    mark = True
                    break
            if not mark:
                real_cnt += 1
        ans = max(real_cnt, ans)
        return
        
    for i in range(idx, 26):
        if not chk[i]:
            chk[i] = 1
            dfs(i, cnt + 1)
            chk[i] = 0

dfs(0, 0)
print(ans)