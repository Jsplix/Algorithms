import sys
input = sys.stdin.readline
# [BOJ] 2953 나는 요리사다 / 수학, 구현, 사칙연산
mx = -1
idx = -1
for i in range(5):
    chk = sum(list(map(int, input().split())))
    if chk > mx:
        idx = i+1
        mx = chk
print(idx, mx)