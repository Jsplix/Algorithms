import sys
input = sys.stdin.readline
# [BOJ] 2170 선 긋기 / 정렬, 스위핑
lines = sorted([tuple(map(int, input().split())) for _ in range(int(input()))])
length = 0

for p1, p2 in lines:
    if not length:
        length = p2 - p1
        pre_p1 = p1
        pre_p2 = p2
        continue

    if p1 >= pre_p1 and p2 <= pre_p2:
        continue

    length += abs(p2-p1)
    if p1 < pre_p2:
        length -= abs(pre_p2-p1)

    pre_p1, pre_p2 = p1, p2
    
print(length)