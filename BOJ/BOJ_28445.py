import sys
input = sys.stdin.readline
# [BOJ] 28445 알록달록 앵무새 / 구현, 자료 구조, 문자열, 정렬
fb, ft = input().split()
mb, mt = input().split()

possible = []
colors = [fb, ft, mb, mt]
for c1 in colors:
    for c2 in colors:
        temp = c1 + ' ' + c2
        if temp not in possible:
            possible.append(temp)

possible.sort()
print(*possible, sep='\n')