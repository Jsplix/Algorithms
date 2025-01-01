import sys
input = sys.stdin.readline
# [BOJ] 22351 수학은 체육과목 입니다 3 / 구현, 문자열, 브루트포스
s = input().rstrip()
mn = 1000
fin = 1000
for i in range(1, len(s)+1):
    temp = s[:i]
    flag = False
    chk = int(temp)

    while len(temp) < len(s):
        chk += 1
        temp += str(chk)
        if temp not in s:
            flag = True
            break
    
    if not flag: 
        mn = min(int(s[:i]), mn)
        fin = min(fin, chk)
print(mn, fin)