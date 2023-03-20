import sys
input = sys.stdin.readline
# [BOJ] 9655 돌 게임 / 수학, DP, 게임 이론
n = int(input())
if n % 2 == 0: print('CY')
else: print('SK')