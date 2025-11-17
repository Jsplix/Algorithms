import sys
input = sys.stdin.readline
# [BOJ] 34704 크기가 4인 박스 / 구현, 그리디
N = int(input())
arr = list(map(int, input().split()))

cnt = [0, 0, 0, 0, 0]
for a in arr:
    cnt[a] += 1

total = cnt[4]

total += cnt[3]
mn3 = min(cnt[1], cnt[3])
cnt[1] -= mn3

total += (cnt[2] // 2)
cnt[2] %= 2

if cnt[2] == 1:
    total += 1
    cnt[1] -= min(2, cnt[1])

if cnt[1]:
    total += (cnt[1] + 3) // 4

print(total)