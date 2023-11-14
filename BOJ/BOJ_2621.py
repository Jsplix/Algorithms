import sys
input = sys.stdin.readline
# [BOJ] 2621 카드게임 / 구현, 많은 조건 분기
colors = {'R': 0, 'B': 0, 'Y': 0, 'G': 0}
num = {i: 0 for i in range(1, 10)}
cards = []
for _ in range(5):
    c, n = input().split()
    colors[c] += 1
    num[int(n)] += 1
    cards.append(int(n))

cards.sort()
cv = sorted(list(colors.values()))
nv = sorted(list(num.items()), key=lambda x:(x[1], x[0]))

score = 0
if cv[-1] == 5:
    flag = True # True - 연속 / False - 비연속
    for i in range(1, 5): # 연속성 확인
        if cards[i-1] + 1 != cards[i]:
            flag = False
            break
    if flag: score = 900 + cards[-1] # 규칙 1
    else: score = 600 + cards[-1] # 규칙 4
elif nv[-1][1] == 4: score = 800 + nv[-1][0] # 규칙 2
elif nv[-1][1] == 3 and nv[-2][1] == 2: score = 700 + nv[-1][0]*10 + nv[-2][0] # 규칙 3
elif nv[-1][1] == 3: score = 400 + nv[-1][0] # 규칙 6
elif nv[-1][1] == 2 and nv[-2][1] == 2: score = 300 + nv[-1][0]*10 + nv[-2][0] # 규칙 7
elif nv[-1][1] == 2: score = 200 + nv[-1][0] # 규칙 8
else:
    flag = True # True - 연속 / False - 비연속
    for i in range(1, 5): # 연속성 확인
        if cards[i-1] + 1 != cards[i]:
            flag = False
            break
    if flag: score = cards[-1] + 500
    else: score = cards[-1] + 100

print(score)