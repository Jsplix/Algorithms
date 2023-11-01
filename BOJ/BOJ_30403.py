from curses.ascii import islower
import sys
input = sys.stdin.readline
# [BOJ] 30403 무지개 만들기 / 구현, 문자열
n = int(input())
s = input().rstrip()

rainbow_lower = {'r': 0, 'o': 0, 'y': 0, 'g': 0, 'b': 0, 'i': 0, 'v': 0}
rainbow_upper = {'R': 0, 'O': 0, 'Y': 0, 'G': 0, 'B': 0, 'I': 0, 'V': 0}

for c in s:
    if c not in rainbow_lower.keys() and c not in rainbow_upper.keys(): continue
    if c.islower(): rainbow_lower[c] += 1
    else: rainbow_upper[c] += 1

lower_flag = False
for k1, v1 in list(rainbow_lower.items()):
    if v1 == 0: lower_flag = True; break

upper_flag = False
for k2, v2 in list(rainbow_upper.items()):
    if v2 == 0: upper_flag = True; break

if not lower_flag and not upper_flag: print("YeS")
elif not lower_flag and upper_flag: print("yes")
elif lower_flag and not upper_flag: print("YES")
else: print("NO!")