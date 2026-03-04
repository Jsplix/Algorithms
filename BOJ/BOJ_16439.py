import sys
input = sys.stdin.readline
# [BOJ] 16439 치킨치킨치킨 / 브루트포스
n, m = map(int, input().split())
preferences = [list(map(int, input().split())) for _ in range(n)]

mx = 0
comb = []
for i in range(m):
    for j in range(i + 1, m):
        # if i == j: continue
        for k in range(j + 1, m):
            # if j == k or k == i: continue
            comb.append((i, j, k))

for a, b, c in comb:
    temp = 0
    for i in range(n):
        temp += max(preferences[i][a], preferences[i][b], preferences[i][c])
    mx = max(mx, temp)
print(mx)