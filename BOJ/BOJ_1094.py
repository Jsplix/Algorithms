import sys
input = sys.stdin.readline
# [BOJ] 1094 막대기 / 수학
n = int(input())
pos_len = [64, 32, 16, 8, 4, 2, 1]
stick = n
chk = 0
for i in range(len(pos_len)):
    if n >= pos_len[i]:
        chk += 1
        n -= pos_len[i]
    
    if n == 0:
        break
print(chk)