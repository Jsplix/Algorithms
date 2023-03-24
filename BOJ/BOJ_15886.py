import sys
input = sys.stdin.readline
# [BOJ] 15886 내 선물을 받아줘 2 / 그래프 이론, 문자열
n = int(input())
move = list(input().rstrip())

answer = 0
for i in range(n-1):
    if move[i] == 'E' and move[i+1] == 'W': answer += 1
print(answer)