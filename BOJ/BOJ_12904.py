import sys
input = sys.stdin.readline
# [BOJ] 12904 A와 B / 구현, 문자열, 그리디
s = list(input().rstrip())
t = list(input().rstrip())

while t: # T를 S로 만들기
    if t[-1] == 'A':
        t.pop()
    elif t[-1] == 'B':
        t.pop()
        t.reverse()
    
    if s == t:
        print(1)
        exit(0)

print(0)