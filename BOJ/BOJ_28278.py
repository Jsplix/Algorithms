import sys
input = sys.stdin.readline
# [BOJ] 28278 스택 2 / 자료 구조, 스택
stk = []
for _ in range(int(input())):
    comm = list(map(int, input().split()))
    if comm[0] == 1:
        stk.append(comm[1])
    elif comm[0] == 2:
        if len(stk) == 0: print(-1)
        else: print(stk.pop())
    elif comm[0] == 3:
        print(len(stk))
    elif comm[0] == 4:
        if len(stk) == 0: print(1)
        else: print(0)
    elif comm[0] == 5:
        if len(stk) == 0: print(-1)
        else: print(stk[-1])