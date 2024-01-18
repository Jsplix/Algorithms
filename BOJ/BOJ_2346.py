import sys
from collections import deque
input = sys.stdin.readline
# [BOJ] 2346 풍선 터뜨리기 / 자료 구조, 덱
n = int(input())
balloons = deque(list(pair) for pair in enumerate(map(int, input().split())))

answer = []
while balloons:
    idx, mv = balloons.popleft()
    answer.append(idx + 1)
    if mv > 0: mv -= 1

    while mv and balloons:
        if mv > 0:
            mv -= 1
            balloons.append(balloons.popleft())
        elif mv < 0:
            mv += 1
            balloons.appendleft(balloons.pop())

print(*answer)