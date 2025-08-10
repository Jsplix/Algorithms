import sys
input = sys.stdin.readline
# [BOJ] 6198 옥상 정원 꾸미기 / 자료 구조, 스택
n = int(input())
buildings = [int(input()) for _ in range(n)]
result = [0 for _ in range(n)]

stk = [n-1]
for i in range(n-2, -1, -1):
    height = buildings[i]
    if height > buildings[stk[-1]]:
        while (stk and height > buildings[stk[-1]]):
            idx = stk.pop()
            result[i] += result[idx] + 1
    stk.append(i)

print(sum(result))