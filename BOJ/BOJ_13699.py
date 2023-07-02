import sys
input = sys.stdin.readline
# [BOJ] 13699 점화식 / DP
n = int(input())
t = [1, 1, 2, 5] + [0 for _ in range(32)]
if n >= 4:
    for i in range(4, 36):
        for j in range(i):
            t[i] += t[j] * t[i-1-j]
print(t[n])