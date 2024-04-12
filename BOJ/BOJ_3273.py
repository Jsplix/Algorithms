import sys
input = sys.stdin.readline
# [BOJ] 3273 두 수의 합 / 정렬, 투 포인터
n = int(input())
arr = sorted(map(int, input().split()))
x = int(input())

l, r = 0, n-1
answer = 0
while l < r:
    check = arr[l] + arr[r]
    if check == x: 
        answer += 1
        l += 1
        r -= 1
    elif check < x:
        l += 1
    elif check > x:
        r -= 1

print(answer)