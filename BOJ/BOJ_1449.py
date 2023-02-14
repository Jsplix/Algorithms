import sys
input = sys.stdin.readline
# [BOJ] 1449 수리공 항승 / 그리디, 정렬
n, l = map(int, input().split())
tape = sorted(list(map(int, input().split())))

left = tape[0]
cnt = 1
for i in range(1, n):
    if tape[i] in range(left, left+l): continue
    else: 
        cnt += 1
        left = tape[i]

print(cnt)