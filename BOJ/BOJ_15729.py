import sys
input = sys.stdin.readline
# [BOJ] 15729 방탈출 / 그리디
# 이러한 유형의 문제 - 이미 지나간 버튼은 상태가 변하지 않음.
n = int(input())
btns = list(map(int, input().split()))
init = [0 for _ in range(n)]

count = 0
for i in range(n):
    if btns[i] != init[i]:
        init[i] ^= 1
        count += 1

        if i + 1 < n:
            init[i+1] ^= 1
        if i + 2 < n:
            init[i+2] ^= 1
    
print(count)