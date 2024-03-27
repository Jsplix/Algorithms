import sys
input = sys.stdin.readline
# [BOJ] 2812 크게 만들기 / 자료 구조, 그리디, 스택
n, k = map(int, input().split())
num = input().rstrip()
stk = []

for x in num:
    while stk and stk[-1] < x and k:
        k -= 1
        stk.pop()
    stk.append(x)

if k: print(''.join(stk[:-k]))
else: print(''.join(stk))