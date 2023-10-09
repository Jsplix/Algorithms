import sys
input = sys.stdin.readline
# [BOJ] 1337 올바른 배열 / 구현, 정렬, 투 포인터
arr = [int(input()) for _ in range(int(input()))]
arr.sort()

chk = []
for i in range(len(arr)):
    cnt = 0
    for j in range(arr[i], arr[i]+5):
        if j not in arr: cnt += 1
    chk.append(cnt)
print(min(chk))