import sys
input = sys.stdin.readline
# [BOJ] 14606 피자 (Small) / 수학, DP
n = int(input())
print(n*(n-1) // 2)