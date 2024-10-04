import sys
from collections import defaultdict
input = sys.stdin.readline
# [BOJ] 9536 여우는 어떻게 울지? / 자료 구조, 문자열, 해시를 사용한 집합과 맵, 파싱
for _ in range(int(input())):
    all = list(input().rstrip().split())
    noise = defaultdict(int)
    while True:
        s = input().rstrip()
        if s == "what does the fox say?": break
        
        temp = list(s.split())[2]
        if noise[temp]: continue
        else: noise[temp] = 1

    result = []
    for word in all:
        if noise[word]: continue
        result.append(word)
    print(*result)