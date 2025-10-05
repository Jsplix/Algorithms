import sys
input = sys.stdin.readline
# [BOJ] 17450 과자 사기 / 수학, 구현, 사칙연산
snacks = [list(map(int, input().split())) for _ in range(3)]
for i in range(3):
    prices = snacks[i][0] * 10
    temp = (snacks[i][1] * 10) / (prices - 500 if snacks[i][0] * 10 >= 5000 else prices)

    snacks[i].append(temp)

mx = max(snacks[0][2], snacks[1][2], snacks[2][2])
if mx == snacks[0][2]: print("S")
elif mx == snacks[1][2]: print("N")
else: print("U")