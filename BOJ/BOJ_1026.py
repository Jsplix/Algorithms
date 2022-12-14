import sys
input = sys.stdin.readline
# [BOJ] 1026 보물 / 그리디 알고리즘, 정렬
n = int(input())
l = list(map(int, input().split()))
r = list(map(int, input().split()))

r.sort()
l.sort(reverse=True)

ans = 0

for i in range(n):
    ans += l[i] * r[i]

print(ans)