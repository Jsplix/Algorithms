import sys
input = sys.stdin.readline
# [BOJ] 9656 돌 게임2 / DP
n = int(input())
if n % 2: print("CY")
else: print("SK")
# 홀수번째 돌을 가져가는 사람 - SK / 짝수번째에 돌을 가져가는 사람 - CY
# 돌은, 1개와 3개씩 밖에 못가져감. 돌의 개수가 홀수이면 상근이가 이기고, 짝수면 창영이가 이김