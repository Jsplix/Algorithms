import sys
input = sys.stdin.readline
# [BOJ] 1919 애너그램 만들기 / 구현, 문자열
a = input().rstrip()
b = input().rstrip()

c = [0 for _ in range(26)]

for c1 in a:
    c[ord(c1)-97]+= 1
for c2 in b:
    c[ord(c2)-97] -= 1

print(sum(map(abs,c)))