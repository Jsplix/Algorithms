# [BOJ] 1256 팰린드롬수 / 구현, 문자열
while True:
    n = input()
    if n == '0':
        break
    if n == n[::-1]:
        print("yes")
    else:
        print("no")