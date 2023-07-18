import sys
input = sys.stdin.readline
# [BOJ] 5800 성적 통계 / 구현, 정렬
cls = [list(map(int, input().split())) for _ in range(int(input()))]
for i in range(1, len(cls)+1):
    cls[i-1][1:] = sorted(cls[i-1][1:])
    print("Class", i)
    mx, mn = cls[i-1][-1], cls[i-1][1]
    gap = -1
    for j in range(1, cls[i-1][0]):
        gap = max(cls[i-1][j+1]-cls[i-1][j], gap)
    print("Max ", mx, ", Min ", mn, ", Largest gap ", gap, sep='')