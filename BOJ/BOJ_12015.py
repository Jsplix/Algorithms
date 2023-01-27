import sys
input = sys.stdin.readline
# [BOJ] 12015 가장 긴 증가하는 부분 수열 2 / 이분 탐색
n = int(input())
arr = list(map(int, input().split()))

chk = [0]

for num in arr:
    if chk[-1] < num:
        chk.append(num)
    else:
        start = 0
        end = len(chk) - 1
        while start <= end:
            mid = (start + end) // 2
            if chk[mid] < num:
                start = mid + 1
            else:
                end = mid - 1
        if start >= len(chk):
            chk.append(num)
        else:
            chk[start] = num

print(len(chk) - 1)