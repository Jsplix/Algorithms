import sys
input = sys.stdin.readline
# [BOJ] 1453 피시방 알바 / 구현
n = int(input())
seats = list(map(int, input().split()))
check = {i: 0 for i in range(1, 101)}

answer = 0
for s in seats:
    if not check[s]:
        check[s] = 1
    else:
        answer += 1
print(answer)