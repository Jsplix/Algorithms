from collections import deque
import sys
input = sys.stdin.readline
# [BOJ] 6137 문자열 생성 / 그리디, 문자열, 투 포인터
n = int(input())
s = deque([])
for i in range(n):
    s.append(input().rstrip())

t = ''
while s != deque([]):
    if ord(s[0]) < ord(s[-1]):
        t += s.popleft()
    elif ord(s[0]) == ord(s[-1]) and len(s) != 1:
        idx = 1
        while True:
            k = len(s)
            if ord(s[0+idx]) < ord(s[k-1-idx]):
                t += s.popleft()
                break
            elif ord(s[0+idx]) == ord(s[k-1-idx]):
                if idx >= k-1-idx:
                    t += s.popleft()
                    break 
                idx += 1
            else:
                t += s.pop()
                break
    else:
        t += s.pop()
    
    if len(t) == 80:
        print(t)
        t = ''
print(t)