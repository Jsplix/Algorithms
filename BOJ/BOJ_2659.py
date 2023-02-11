from collections import deque
import sys
input = sys.stdin.readline
# [BOJ] 2659 십자카드 문제 / 구현, 브루트 포스
def check_clock(n: deque):
    chk = []
    for i in range(4):
        chk.append(int(''.join(map(str, n))))
        n.appendleft(n.pop())
    return min(chk)

num = deque(list(map(int, input().split())))    
clock_num = check_clock(num)

cnt = 1
for i in range(1111, clock_num):
    if '0' not in str(i) and i == check_clock(deque(list(map(int, str(i))))):
        cnt += 1
print(cnt)