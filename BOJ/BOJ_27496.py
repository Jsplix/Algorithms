import sys
input = sys.stdin.readline
# [BOJ] 27496 발머의 피크 이론 / 누적 합, 슬라이딩 윈도우
n, l = map(int, input().split())
alcohol = list(map(int, input().split()))
blc = 0
count, idx = 0, 0
for i in range(l):
    blc += alcohol[i]
    if 129 <= blc <= 138: count += 1

for i in range(l, n):
    blc += alcohol[i]
    blc -= alcohol[idx]
    idx += 1
    if 129 <= blc <= 138: count += 1

print(count)