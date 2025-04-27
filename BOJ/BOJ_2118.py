import sys
from itertools import accumulate
input = sys.stdin.readline
# [BOJ] 2118 두 개의 탑 / 투 포인터, 누적합
n = int(input())
distance = [int(input()) for _ in range(n)]
acc_sum = [*accumulate(distance)]

total = acc_sum[-1]
i, j = 0, 0
mx = 0
while i < n and j < n:
    clock = acc_sum[j]-acc_sum[i]
    counter_clock = total - acc_sum[j] + acc_sum[i]
    gap = min(clock, counter_clock)
    if gap > mx:
        mx = gap
    
    if clock < counter_clock:
        j += 1
    else:
        i += 1
print(mx)