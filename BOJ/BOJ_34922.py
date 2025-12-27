import sys
import math
input = sys.stdin.readline
# [BOJ] 34922 사각지대 / 수학, 기하학
PI = math.pi
w, h = map(int, input().split())
r = int(input())
print((w * h) - ((PI * r ** 2) / 4))