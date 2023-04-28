import sys
input = sys.stdin.readline
# [BOJ] 1356 유진수 / 수학, 구현, 브루트 포스, 문자열
n = input().rstrip()
if len(n) == 1: print("NO")
else:
    flag = False
    for i in range(1, len(n)):
        l = n[:i]
        r = n[i:]

        m1, m2 = 1, 1
        for x1 in l:
            x1 = int(x1)
            m1 *= x1
        for x2 in r:
            x2 = int(x2)
            m2 *= x2
        
        if m1 == m2: flag = True; break
        else: continue
    
    if flag: print("YES")
    else: print("NO")