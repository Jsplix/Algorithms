import sys
input = sys.stdin.readline
# [BOJ] 32684 장기 / 수학, 구현, 사칙연산
c = list(map(int, input().split()))
h = list(map(int, input().split()))

sm_cho = 13 * c[0] + 7 * c[1] + 5 * c[2] + 3 * c[3] + 3 * c[4] + 2 * c[5] + 72
sm_han = 13 * h[0] + 7 * h[1] + 5 * h[2] + 3 * h[3] + 3 * h[4] + 2 * h[5] + 73

if (sm_cho > sm_han): print("cocjr0208")
else: print("ekwoo")