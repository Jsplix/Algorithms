import sys
input = sys.stdin.readline
# [BOJ] 31395 정렬된 연속한 부분수열의 개수 / 수학, 조합론
n = int(input())
arr = list(map(int, input().split()))

idx, k = 0, 0
prevNum = 0
answer = 0

while n:
    if arr[idx] > prevNum:
        k += 1
    else:
        answer += ((k + 1) * k) // 2
        k = 1
    prevNum = arr[idx]
    n -= 1
    idx += 1

answer += ((k + 1) * k) // 2
print(answer)