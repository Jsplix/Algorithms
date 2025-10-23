import sys
input = sys.stdin.readline
# [BOJ] 18406 럭키 스트레이트 / 구현, 문자열
N = list(map(int, input().rstrip()))
left = sum(N[:len(N) // 2])
right = sum(N[len(N) // 2:])

if left == right: print("LUCKY")
else: print("READY")