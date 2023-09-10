import sys
input = sys.stdin.readline
# [BOJ] 20546 🐜 기적의 매매법 🐜 / 구현, 시뮬레이션
cash = int(input())
MachineDuck = list(map(int, input().split()))

up_cnt, dwn_cnt = 0, 0
s, j = cash, cash
s_buy, j_buy = 0, 0
for i in range(14):
    if MachineDuck[i] <= s: # 준현 매수
        j_buy += j // MachineDuck[i]
        j %= MachineDuck[i]
    
    if i == 0: continue
    
    if MachineDuck[i-1] > MachineDuck[i]: dwn_cnt += 1; up_cnt = 0
    elif MachineDuck[i-1] < MachineDuck[i]: up_cnt += 1; dwn_cnt = 0

    if dwn_cnt == 3: # 전량 매수
        s_buy += s // MachineDuck[i]
        s %= MachineDuck[i]
    if up_cnt == 3: # 전량 매매
        s += (s_buy) * MachineDuck[i]
        s_buy = 0

total_s, total_j = s + (s_buy * MachineDuck[-1]), j + (j_buy * MachineDuck[-1])
if total_s < total_j: print("BNP")
else:
    if total_s == total_j: print("SAMESAME")
    else: print("TIMING")