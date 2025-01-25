import sys
from collections import deque
input = sys.stdin.readline
# [BOJ] 5397 키로거 / 자료 구조, 스택, 연결 리스트
for _ in range(int(input())):
    password, stk = [], deque([])
    pressed_keys = input().rstrip()
    now = 0
    for key in pressed_keys:
        if key == '<':
            if not password: continue
            else:
                stk.appendleft(password.pop())
        elif key == '>':
            if not stk: continue
            else: 
                password.append(stk.popleft())
        elif key == '-':
            if password: password.pop()
            else: continue
        else:
            password.append(key)

    print(''.join(password)+''.join(stk))