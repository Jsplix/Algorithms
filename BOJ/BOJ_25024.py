import sys
input = sys.stdin.readline
# [BOJ] 25024 시간과 날짜 / 구현
for _ in range(int(input())):
    x, y = map(int, input().split()) # x - 시, 월 / y - 분, 일

    result = []
    if x <= 23 and y <= 59: result.append("Yes")
    else: result.append("No")

    if 1 <= x <= 12 and 1 <= y <= 31:
        if y <= 31 and x in [1, 3, 5, 7, 8, 10, 12]: result.append("Yes")
        elif y <= 30 and x != 2: result.append("Yes")
        elif y <= 29 and x == 2: result.append("Yes")
        else: result.append("No")
    else:
        result.append("No")
    
    print(*result)