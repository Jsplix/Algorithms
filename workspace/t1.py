import sys
input = sys.stdin.readline

n = int(input())
board = []
for i in range(n):
    board.append(list(map(int, input().split())))

