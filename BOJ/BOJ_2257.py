import sys
input = sys.stdin.readline
# [BOJ] 2257 화학식량 / 자료 구조, 문자열, 스택
mass = {'H': 1, 'C': 12, 'O': 16}
chemical = input().rstrip()

stk = []
for c in chemical:
    if c == '(': stk.append(c)
    elif c in mass.keys():
        stk.append(mass[c])
    elif c == ')':
        temp = 0
        while True:
            if stk[-1] == '(':
                stk.pop()
                stk.append(temp)
                break
            else:
                temp += stk.pop()
    else:
        stk.append(stk.pop() * int(c))
print(sum(stk))