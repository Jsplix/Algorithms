import sys
input = sys.stdin.readline
# [BOJ] 32278 선택 가능성이 가장 높은 자료형 / 구현
n = int(input())
if (-2)**15 <= n < 2**15:
    print("short")
elif (-2)**31 <= n < 2**31:
    print("int")
else:
    print("long long")