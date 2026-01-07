import sys
input = sys.stdin.readline
# [BOJ] 1477 휴게소 세우기 / 이분 탐색, 매개변수 탐색
N, M, L = map(int, input().split())
p = [0] + list(map(int, input().split())) + [L]

p.sort()
diff = []
for i in range(1, N + 2):
    diff.append(p[i] - p[i - 1])

left, right = 1, L - 1
while left <= right:
    mid = (left + right) // 2

    chk = 0
    for i in range(len(diff)):
        if mid < diff[i]:
            chk += ((diff[i] - 1) // mid)
    
    if chk <= M:
        right = mid - 1
    else:
        left = mid + 1

print(left)