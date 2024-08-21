import sys
input = sys.stdin.readline
# [BOJ] 17094 Serious Problem / 구현, 문자열
le = int(input())
s = input().rstrip()

a = s.count('2')
b = s.count('e')

if a == b:
    print("yee")
elif a > b:
    print("2")
else:
    print("e")