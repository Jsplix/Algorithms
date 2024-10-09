import sys
input = sys.stdin.readline
# [BOJ] 2290 LCD Test / 구현, 문자열
s, n = input().split()

s = int(s)
display = ['' for _ in range(2*s+3)]
for i in range(len(n)):
    temp = []
    for j in range(2*s+3):
        if n[i] == '1':
            if j == 0 or j == s+1 or j == (2*s+2): temp.append(' '*(s+2))
            else: temp.append(' '*(s+1) + '|')
        elif n[i] == '4':
            if j == 0 or j == (2*s+2): temp.append(' '*(s+2))
            elif 0 < j < s+1: temp.append('|' + ' '*s + '|')
            elif j == s+1: temp.append(' ' + '-'*s + ' ')
            else: temp.append(' '*(s+1) + '|')
        elif n[i] == '7':
            if j == 0: temp.append(' ' + '-'*s + ' ')
            elif j == s+1 or j == 2*s+2: temp.append(' '*(s+2))
            else: temp.append(' '*(s+1) + '|')
        elif n[i] == '0':
            if j == 0 or j == (2*s+2): temp.append(' ' + '-'*s + ' ')
            elif j == s+1: temp.append(' '*(s+2))
            else: temp.append('|' + ' '*s + '|')
        else:
            if j == 0 or j == s+1 or j == (2*s+2): 
                temp.append(' ' + '-'*s + ' ')
                continue
            else:
                if n[i] == '2':
                    if 0 < j < s+1: temp.append(' '*(s+1) + '|')
                    else: temp.append('|' + ' '*(s+1))
                elif n[i] == '3':
                    temp.append(' '*(s+1) + '|')
                elif n[i] == '5':
                    if 0 < j < s+1: temp.append('|' + ' '*(s+1))
                    else: temp.append(' '*(s+1) + '|')
                elif n[i] == '6':
                    if 0 < j < s+1: temp.append('|' + ' '*(s+1))
                    else: temp.append('|' + ' '*s + '|')
                elif n[i] == '8':
                    temp.append('|' + ' '*s + '|')
                elif n[i] == '9':
                    if 0 < j < s+1: temp.append('|' + ' '*s + '|')
                    else: temp.append(' '*(s+1) + '|')
    
    for k in range(2*s+3):
        display[k] += temp[k] + ' '

for line in display:
    print(line)