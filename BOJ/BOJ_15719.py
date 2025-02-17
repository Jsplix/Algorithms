import sys
input = sys.stdin.readline
# [BOJ] 15719 중복된 숫자 / 수학, 구현
n = int(input())
sm = sum(range(1, n))
arr = input().rstrip()

check, temp = 0, ""
for a in arr:
    if a.isdigit():
        temp += a
    elif a == " ":
        check += int(temp)
        temp = ""

check += int(temp)
print(abs(sm-check))