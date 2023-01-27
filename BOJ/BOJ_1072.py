import sys
input = sys.stdin.readline
# [BOJ] 1072 게임 / 이분 탐색
x, y = map(int, input().split())
z = (y * 100) // x

if z >= 99:
    ans = -1
else:
    start = 0
    end = x

    while start <= end:
        mid = (start + end) // 2
        if (y + mid) * 100 // (x + mid) <= z:
            start = mid + 1
        else:
            ans = mid
            end = mid - 1

print(ans)