from math import gcd
import sys
input = sys.stdin.readline
# [BOJ] 2485 가로수 / 수학, 정수론, 유클리드 호제법
n = int(input())
trees = list(int(input()) for _ in range(n))

gap = []
for i in range(n-1):
    gap.append(trees[i+1]-trees[i])

g = gap[0]
for j in range(1, n-1):
    g = gcd(g, gap[j])

answer = 0
for btw in gap:
    answer += btw // g - 1
print(answer)