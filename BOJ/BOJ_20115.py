import sys
input = sys.stdin.readline
# [BOJ] 20115 에너지 드링크 / 그리디
n = int(input())
energy_drink = sorted(list(map(int, input().split())))
rest_sum = sum(energy_drink[:n-1])
print(rest_sum / 2 + max(energy_drink))