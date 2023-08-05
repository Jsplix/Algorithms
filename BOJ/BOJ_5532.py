from math import ceil
import sys
input = sys.stdin.readline
# [BOJ] 5532 방학 숙제 / 수학, 사칙연산
day = [int(input()) for _ in range(5)]
hw = max(ceil(day[1] / day[3]), ceil(day[2] / day[4]))
print(day[0] - hw)