import sys
from collections import defaultdict
input = sys.stdin.readline
# [BOJ] 1283 단축키 지정 / 구현, 문자열
check = defaultdict(int)
for _ in range(int(input())):
    word = list(input().rstrip().split())

    selected = -1
    for i in range(len(word)):
        if not check[word[i][0].lower()] and not check[word[i][0].upper()]:
            selected = (i, 0)
            check[word[i][0]] = 1
            break

    if selected == -1:
        for i in range(len(word)):
            for j in range(len(word[i])):
                if not check[word[i][j].lower()] and not check[word[i][j].upper()]:
                    selected = (i, j)
                    check[word[i][j]] = 1
                    break

            if selected != -1:
                break

    
    if selected == -1:
        print(*word)
    else:
        for i in range(len(word)):
            for j in range(len(word[i])):
                if (i, j) == selected:
                    print('[', word[i][j], ']', sep='', end='')
                else:
                    print(word[i][j], end='')
            print(" ", end='')
        print()