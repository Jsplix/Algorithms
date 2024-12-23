import sys
input = sys.stdin.readline
# [BOJ] 21612 Boiling Water / 수학, 구현, 사칙연산
result = 5 * int(input()) - 400
if result < 100: print(result, 1, sep='\n')
elif result == 100: print(result, 0, sep='\n')
else: print(result, -1, sep='\n')