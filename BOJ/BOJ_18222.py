import sys
input = sys.stdin.readline
# [BOJ] 18222 투에-모스 문자열 / 재귀, 분할 정복
# 풀이 - 짝수번째 값은 그대로, 홀수번째 값은 반전시킴
def solve(val):
    if val == 0: return 0
    elif val == 1: return 1
    elif not (val % 2): return solve(val // 2)
    else: return 1 - solve(val // 2)

print(solve(int(input())-1))