import sys
input = sys.stdin.readline
# [BOJ] 1253 좋다 / 자료 구조, 정렬, 이분 탐색, 투 포인터
n = int(input())
arr = sorted(list(map(int, input().split())))

answer = 0
for i in range(n):
    now = arr[i]
    left = 0
    right = n - 1
    while left < right:
        if arr[left] + arr[right] == now:
            if left == i: left += 1
            elif right == i: right -= 1
            else: answer += 1 ; break
        elif arr[left] + arr[right] < now:
            left += 1
        else:
            right -= 1

print(answer)