import sys
input = sys.stdin.readline
# [BOJ] 2437 저울 / 그리디, 정렬
n = int(input())
arr = sorted(list(map(int, input().split())))

answer = 1
for x in arr:
    if answer < x:
        break
    answer += x
print(answer)