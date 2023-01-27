import sys
input = sys.stdin.readline
# [BOJ] 1004 어린왕자 / 기하
t = int(input())
for _ in range(t):
    x1, y1, x2, y2 = map(int, input().split())
    s = int(input())
    cnt = 0
    for i in range(s):
        cx, cy, r = map(int, input().split())
        dist_1 = ((x1 - cx)**2 + (y1 - cy)**2) ** 0.5
        dist_2 = ((x2 - cx)**2 + (y2 - cy)**2) ** 0.5
        if (dist_1 < r and dist_2 > r) or (dist_1 > r and dist_2 < r):
            cnt += 1
    print(cnt)