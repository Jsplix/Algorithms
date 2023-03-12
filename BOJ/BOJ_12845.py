import sys
input = sys.stdin.readline
# [BOJ] 12845 모두의 마블 / 그리디 알고리즘
# 가장 큰 수로 시작하면 순서 상관없이 최댓값을 구할 수 있음
n = int(input())
cards = sorted(list(map(int, input().split())), reverse=True)
sm = 0
for i in range(1, n):
    sm += (cards[0] + cards[i])
print(sm)