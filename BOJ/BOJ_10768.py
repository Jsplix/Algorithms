import sys
input = sys.stdin.readline
# [BOJ] 10768 특별한 날 / 구현
month = int(input())
day = int(input())

if month < 2:
    print("Before")
elif month == 2:
    if day == 18:
        print("Special")
    elif day < 18:
        print("Before")
    else:
        print("After")
else: print("After")