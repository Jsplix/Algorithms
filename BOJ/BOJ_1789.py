import sys
input = sys.stdin.readline
# [BOJ] 1789 수들의 합 / 그리디, 수학
s = int(input())
sm = 0
idx = 0
# N이 최대가 되는 방법은 1에서부터 해당 합이 s가 되는 N까지임
# N은 다음 1~N까지의 합 전까지는 자기 자신이 최대임 
# (ex, 55까지의 최대 N = 10, 56에서도 10, 57에서도 10, 하지만, 11이 더해지는 66일때 N=11이 됨)
if s == 1:
    print(1)
else:
    while sm + idx <= s:
        sm += idx
        idx += 1
    print(idx-1)