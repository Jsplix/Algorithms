import sys
input = sys.stdin.readline
# [BOJ] 2711 오타맨 고창영 / 구현, 문자열
for _ in range(int(input())):
    pos, word = input().rstrip().split()
    pos = int(pos)
    word = list(word)
    word.pop(pos-1)
    print(''.join(word))