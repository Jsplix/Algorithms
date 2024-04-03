import sys
input = sys.stdin.readline
# [BOJ] 17070 파이프 옮기기 1 / DP, 그래프 탐색, 그래프 이론
def OOB(r, c):
    global n
    if 0 <= r < n and 0 <= c < n and room[r][c] != 1: return True
    else: return False

def push(dir, r, c):
    # dir - 현재 파이프의 방향
    global n, answer
    if r == n-1 and c == n-1: 
        answer += 1
        return

    if dir == 0: # 가로
        if c == n-1: return
        if OOB(r, c+1): 
            # room[r][c+1] = 3
            push(dir, r, c+1)

        if OOB(r+1, c+1) and OOB(r+1, c) and OOB(r, c+1): 
            # room[r+1][c+1] = 3
            push(dir+2, r+1, c+1)

    elif dir == 1: # 세로
        if r == n-1: return
        if OOB(r+1, c): 
            # room[r+1][c] = 3
            push(dir, r+1, c)

        if OOB(r+1, c+1) and OOB(r+1, c) and OOB(r, c+1): 
            # room[r+1][c+1] = 3
            push(dir+1, r+1, c+1)

    elif dir == 2: # 대각선
        if OOB(r+1, c+1) and OOB(r+1, c) and OOB(r, c+1): 
            # room[r+1][c+1] = 3
            push(dir, r+1, c+1)

        if OOB(r+1, c): 
            # room[r+1][c] = 3
            push(dir-1, r+1, c)

        if OOB(r, c+1): 
            # room[r][c+1] = 3
            push(dir-2, r, c+1)


# 이미 지나온 길로는 다시 못 돌아감.
n = int(input())
room = [list(map(int, input().split())) for _ in range(n)]
# room[0][0], room[0][1] = 2, 2
answer = 0

push(0, 0, 1)
print(answer)