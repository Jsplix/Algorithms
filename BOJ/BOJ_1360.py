import sys
input = sys.stdin.readline
# [BOJ] 1360 되돌리기 / 구현
history = []
def add(ch: str):
    global now
    now += ch

def undo(frm: int, time: int):
    global now
    flag = False
    for i in range(len(history)-1, -1, -1):
        if history[i][0] >= frm - time:
            continue
        flag = True
        now = history[i][1]
        history.append([frm, now])
        break
    
    if not flag:
        now = ''
        history.append([frm, now])

now = ''
for _ in range(int(input())):
    temp = list(input().split())
    if temp[0] == "type":
        add(temp[1])
        history.append([int(temp[2]), now])
    else:
        undo(int(temp[2]), int(temp[1]))
    
print(history[-1][1])