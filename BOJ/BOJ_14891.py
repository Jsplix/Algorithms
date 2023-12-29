import sys
from collections import deque
input = sys.stdin.readline
# [BOJ] 14891 톱니바퀴 / 구현, 시뮬레이션
def rotation(lst: deque, dir):
    if dir == -1:
        lst.append(lst.popleft())
    elif dir == 1:
        lst.appendleft(lst.pop())

n_score = {'0': 0, '1': 0, '2': 0, '3': 0}
s_score = {'0': 1, '1': 2, '2': 4, '3': 8}
wheel = [deque(input().rstrip()) for _ in range(4)] # 2번과 6번 인덱스가 이웃한 톱니바퀴와 맞닿음
for _ in range(int(input())):
    n, d = map(int, input().split())
    n -= 1
    # 맞닿은 부분의 극이 같다면 회전시키지 않음 / 다르다면 반대방향으로 회전시킴
    if n == 0:
        if wheel[n][2] != wheel[n+1][6]:
            if wheel[n+1][2] != wheel[n+2][6]:
                if wheel[n+2][2] != wheel[n+3][6]:
                    rotation(wheel[n+3], d*-1*-1*-1)
                rotation(wheel[n+2], d*-1*-1)
            rotation(wheel[n+1], d*-1)
    elif n == 1:
        if wheel[n-1][2] != wheel[n][6]:
            rotation(wheel[n-1], d*-1)
        if wheel[n][2] != wheel[n+1][6]:
            if wheel[n+1][2] != wheel[n+2][6]:
                rotation(wheel[n+2], d*-1*-1)
            rotation(wheel[n+1], d*-1)
    elif n == 2:
        if wheel[n-1][2] != wheel[n][6]:
            if wheel[n-2][2] != wheel[n-1][6]:
                rotation(wheel[n-2], d*-1*-1)
            rotation(wheel[n-1], d*-1)
        if wheel[n][2] != wheel[n+1][6]:
            rotation(wheel[n+1], d*-1)
    elif n == 3:
        if wheel[n][6] != wheel[n-1][2]:
            if wheel[n-1][6] != wheel[n-2][2]:
                if wheel[n-2][6] != wheel[n-3][2]:
                    rotation(wheel[n-3], d*-1*-1*-1)
                rotation(wheel[n-2], d*-1*-1)
            rotation(wheel[n-1], d*-1)
    rotation(wheel[n], d)

answer = 0
for i in range(4):
    if wheel[i][0] == '0': answer += n_score[str(i)]
    elif wheel[i][0] == '1': answer += s_score[str(i)]
print(answer)