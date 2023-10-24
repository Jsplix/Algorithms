import sys
input = sys.stdin.readline
# [BOJ] 1755 숫자놀이 / 문자열, 정렬
d = {'0': 'zero', '1': 'one', '2': 'two', '3': 'three', '4': 'four', '5': 'five',
     '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine'}
total = {}

m, n = input().split()

for i in range(10):
    eng = ''
    for j in range(10):
        if i != 0: eng = d[str(i)] + ' '
        else: eng = ''
        cur = 10*i + j
        eng += d[str(j)]
        total[cur] = eng

answer = []
for k in range(int(m), int(n)+1):
    answer.append((k, total[k]))
answer.sort(key=lambda x:x[1])

for x in range(len(answer)):
    print(answer[x][0], end=' ')
    if x % 10 == 9: print('')