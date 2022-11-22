import sys
input = sys.stdin.readline
# [BOJ] N-Queen / 백트래킹
def is_promising(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x] - row[i]) == x - i:
            return False
    return True

def back(x):
    global cnt
    if x == n:
        cnt += 1
    else:
        for i in range(n):
            row[x] = i
            if is_promising(x):
                back(x + 1)

n = int(input())
cnt = 0
row = [0] * n
back(0)
print(cnt)