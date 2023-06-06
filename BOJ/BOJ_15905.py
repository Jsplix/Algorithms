import sys
input = sys.stdin.readline
# [BOJ] 15905 스텔라(STELLA)가 치킨을 선물했어요 / 구현, 정렬
scores = [list(map(int, input().split())) for _ in range(int(input()))]
scores.sort(key=lambda x:(-x[0], -x[1]))

last = scores[4][0]
answer = 0

for i in range(5, len(scores)):
    if scores[i][0] == last: answer += 1
    else: break

print(answer)