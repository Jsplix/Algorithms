import sys
input = sys.stdin.readline
# [BOJ] 2238 경매 / 구현
u, n = map(int, input().split())
person = [[] for _ in range(u+1)]
cnt = [0 for _ in range(u+1)]

for _ in range(n):
    s, p = input().split()
    p = int(p)
    cnt[p] += 1
    person[p].append(s)

mn = n + 1
for i in range(1, u+1):
    if cnt[i]:
        mn = min(mn, cnt[i])

for i in range(1, u+1):
    if mn == cnt[i]:
        print(person[i][0], i)
        break