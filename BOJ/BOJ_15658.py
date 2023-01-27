import sys
input = sys.stdin.readline
# [BOJ] 15658 연산자 끼워넣기(2) / 브루트 포스, 재귀, 백트래킹
n = int(input())
num_list = list(map(int, input().split()))
oper_list = list(map(int, input().split()))

chk = []

def solve(idx, v, add, sub, mul, div):
    if idx == n:
        chk.append(v)
        return
    
    if add > 0:
        solve(idx + 1, v + num_list[idx], add - 1, sub, mul, div)
    if sub > 0:
        solve(idx + 1, v - num_list[idx], add, sub - 1, mul, div)
    if mul > 0:
        solve(idx + 1, v * num_list[idx], add, sub, mul - 1, div)
    if div > 0:
        solve(idx + 1, v // num_list[idx] if v > 0 else -((-v) // num_list[idx]), add, sub, mul, div - 1)

# 이러한 방식의 재귀 백트래킹도 있다.

solve(1, num_list[0], oper_list[0], oper_list[1], oper_list[2], oper_list[3])
print(str(max(chk)) + '\n' + str(min(chk)))