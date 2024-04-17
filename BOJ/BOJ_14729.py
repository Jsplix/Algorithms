import sys
input = sys.stdin.readline
# [BOJ] 14729 칠무해 / 정렬
scores = sorted(float(input()) for _ in range(int(input())))
for i in range(7):
    print("%.3f" % scores[i])