import sys
input = sys.stdin.readline
# [BOJ] 1662 압축 / 자료 구조, 스택, 재귀
stk = []
a, val = 0, ''
for c in input().rstrip():
    if c == '(':
        stk.append([a-1, val])
        a = 0
        val = ''
    elif c == ')':
        k = stk.pop()
        a = int(k[1][-1]) * a + k[0]
        val = ''
    else:
        val += c
        a += 1
print(a)