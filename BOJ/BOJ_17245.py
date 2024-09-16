import sys
input = sys.stdin.readline
# [BOJ] 17245 서버실 / 이분 탐색, 매개 변수 탐색
n = int(input())
room = []
total, mx = 0, -1
for _ in range(n):
    line = list(map(int, input().split()))
    room.append(line)
    total += sum(line)
    mx = max(mx, max(line))

left, right = 0, mx
check = []
while left <= right:
    mid = (left + right) // 2

    temp = 0
    for i in range(n):
        for j in range(n):
            if room[i][j] <= mid:
                temp += room[i][j]
            else:
                temp += mid
    
    if total / 2 <= temp:
        check.append(mid)
        right = mid - 1
    else:
        left = mid + 1

print(min(check))