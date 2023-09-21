import sys
input = sys.stdin.readline
# [BOJ] 16987 계란으로 계란치기 / 브루트포스, 백트래킹
n = int(input())
eggs = [list(map(int, input().split())) for _ in range(n)]
# 내구도는 상대 계란의 무게 만큼 깎임 -> 내구도 0 이하되면 계란 깨짐
answer = 0
def back(idx):
    global answer
    if idx == n:
        chk = 0
        for k in range(n):
            if eggs[k][0] <= 0:
                chk += 1
        answer = max(answer, chk)
        return

    if eggs[idx][0] <= 0:
        back(idx + 1)
        return
    
    flag = False
    for i in range(n):
        if i == idx: continue
        if eggs[i][0] > 0: flag = True; break

    if not flag:
        answer = max(answer, n-1)
        return
    
    for j in range(n):
        if j == idx or eggs[j][0] <= 0: continue
        eggs[idx][0] -= eggs[j][1]
        eggs[j][0] -= eggs[idx][1]
        back(idx+1)
        eggs[idx][0] += eggs[j][1]
        eggs[j][0] += eggs[idx][1]

back(0)
print(answer)