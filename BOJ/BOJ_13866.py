import sys
input = sys.stdin.readline
# [BOJ] 13866 팀 나누기 / 수학, 구현, 사칙연산
players = sorted(list(map(int, input().split())))
a = players[0] + players[-1]
b = players[1] + players[2]
print(abs(a-b))