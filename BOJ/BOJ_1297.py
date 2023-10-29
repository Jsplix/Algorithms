from math import sqrt
import sys
input = sys.stdin.readline
# [BOJ] 1297 TV 크기 / 기하학, 피타고라스 정리
d, h, w = map(int, input().split())
ratio = d/sqrt((h**2)+(w**2))
print(int(h*ratio), int(w*ratio))