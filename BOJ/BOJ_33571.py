import sys
input = sys.stdin.readline
# [BOJ] 33571 구멍 / 구현, 문자열
s = input().rstrip()
d = {chr(i): 0 for i in range(ord('a'), ord('z')+1)}
temp = {chr(i): 0 for i in range(ord('A'), ord('Z')+1)}
d.update(temp)
d['@'] = 1
d['A'], d['a'], d['b'], d['D'], d['d'], d['e'], d['g'], d['O'], d['o'], d['P'], d['p'], d['Q'], d['q'], d['R'] = 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1
d['B'] = 2
result = 0
for c in s:
    if c == ' ': continue
    result += d[c]

print(result)