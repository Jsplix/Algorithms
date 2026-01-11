import sys
input = sys.stdin.readline
# [BOJ] 30224 Lucky 7 / 수학, 구현
n = input().rstrip()
num = int(n)

if '7' not in n and num % 7 != 0:
    print("0")
elif '7' not in n and num % 7 == 0:
    print("1")
elif '7' in n and num % 7 != 0:
    print("2")
else:
    print("3")