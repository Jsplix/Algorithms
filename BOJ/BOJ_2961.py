import sys
input = sys.stdin.readline
# [BOJ] 2961 도영이가 만든 맛있는 음식 / 브루트 포스, 비트마스킹, 백트래킹
def back(len, idx):
    global w, answer
    if len == w:
        sourness = 1
        bitterness = 0
        for k in chk:
            sourness *= k[0]
            bitterness += k[1]
        answer = min(answer, abs(sourness-bitterness))
        return
    
    for i in range(idx, n):
        chk.append(li[i])
        back(len+1, i+1)
        chk.pop()

n = int(input())
li = [list(map(int, input().split())) for _ in range(n)]
answer = 10**9
chk = []

for i in range(1, n+1):
    w = i
    back(0, 0)
print(answer)