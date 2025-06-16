import sys
input = sys.stdin.readline
# [BOJ] 14623 감정이입 / 수학, 구현
b1 = int(input().rstrip(), 2)
b2 = int(input().rstrip(), 2)

print(bin(b1*b2)[2:])