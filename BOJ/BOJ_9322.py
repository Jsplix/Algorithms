import sys
input = sys.stdin.readline
# [BOJ] 9322 철벽 보안 알고리즘 / 자료 구조, 문자열, 해시 사용 집합과 맵
for _ in range(int(input())):
    words = int(input())
    first_key = list(input().split())
    second_key = list(input().split())
    secret = list(input().split())
    # c = {}
    
    order = []
    for c in second_key:
        order.append(first_key.index(c))
    
    answer = []
    for i in range(words):
        answer.append((secret[i], order[i]))
    answer.sort(key=lambda x: x[1])
    for i in range(words):
        print(answer[i][0], end=' ')
    print('')