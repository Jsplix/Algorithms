import sys
input = sys.stdin.readline
# [BOJ] 6888 Terms of Office / 수학, 정수론
x = int(input())
y = int(input())

while x <= y:
    print("All positions change in year", x)
    x += 60