import sys
input = sys.stdin.readline
# [BOJ] 5543 상근날드 / 수학, 사칙연산
burger = [int(input()) for _ in range(3)]
drink = [int(input()) for _ in range(2)]
print(min(burger)+min(drink)-50)