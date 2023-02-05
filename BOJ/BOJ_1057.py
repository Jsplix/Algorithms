import sys
input = sys.stdin.readline
# [BOJ] 1057 토너먼트 / 수학
n, j, h = map(int, input().split())
round = 0
while j != h:
    j -= j//2
    h -= h//2
    round += 1
print(round)