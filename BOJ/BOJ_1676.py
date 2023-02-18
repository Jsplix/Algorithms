import sys
input = sys.stdin.readline
# [BOJ] 1676 팩토리얼 0의 개수 / 수학
n = int(input())

div5 = n // 5
div25 = n // 25
div125 = n // 125

print(div5 + div25 + div125)