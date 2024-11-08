import sys
input = sys.stdin.readline
# [BOJ] 3495 아스키 도형 / 구현, 기하학
h, w = map(int, input().split())
v = []
area = 0
for i in range(h):
    line = input().rstrip()
    for c in line:
        if c == "/" or c == "\\":
            if len(v):
                area += 0.5
                v.pop()
            else:
                area += 0.5
                v.append(c)
        else:
            if len(v):
                area += 1
print(int(area))