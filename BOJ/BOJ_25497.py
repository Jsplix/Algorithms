from curses.ascii import isalpha
import sys
input = sys.stdin.readline
# [BOJ] 25497 기술 연계마스터 임스 / 구현, 자료 구조, 스택
skill = {str(i):0 for i in range(1, 10)}
skill['L'], skill['R'], skill['S'], skill['K'] = 0, 0, 0, 0

n = int(input())
comm = input().rstrip()

cnt = 0
for cm in comm:
    if cm.isalpha():
        if cm == 'L' or cm == 'S':
            skill[cm] += 1
        else: 
            if cm == 'R' and skill['L']: 
                cnt += 1
                skill['L'] -= 1
            elif cm == 'K' and skill['S']: 
                cnt += 1
                skill['S'] -= 1
            else: break
    else:
        cnt += 1

print(cnt)