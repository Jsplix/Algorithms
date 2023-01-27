import sys
input = sys.stdin.readline
# [BOJ] N-Queen / 백트래킹
def is_promising(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x] - row[i]) == x - i:
            # 대각선 확인 -> (행 - 행) == (열 - 열)
            return False
    return True

def back(x):
    global cnt
    if x == n:
        cnt += 1
    else:
        for i in range(n): # i는 열번호
            row[x] = i
            if is_promising(x):
                back(x + 1)

n = int(input())
cnt = 0
row = [0] * n # Queen의 위치
back(0)
print(cnt)