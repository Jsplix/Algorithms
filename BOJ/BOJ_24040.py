import sys
input = sys.stdin.readline
# [BOJ] 24040 예쁜 케이크 / 수학, 정수론
for test_case in range(int(input())):
    n = int(input())
    if not n % 9: print("TAK")
    elif n % 3 == 2: print("TAK")
    else: print("NIE")

# n은 넓이이며, 예쁜 케이크를 만들기 위해서는 둘레의 길이가 3의 배수여야 함.
# 가로, 세로의 길이를 각각 (3a+x), (3b+y)라고 두면 (x, y는 3으로 나눈 나머지)
# (3a+x)+(3b+y) 가 3의 배수가 되면 됨 (--> xy == 2 (1,2), (2,1) or 0 (0, 0)이 되면 됨)