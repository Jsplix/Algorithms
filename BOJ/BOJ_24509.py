import sys
input = sys.stdin.readline
# [BOJ] 24509 상품의 주인은? / 구현, 정렬
korean, english, math, science = [], [], [], []
reward = []
for _ in range(int(input())):
    num, k, e, m, s = map(int, input().split())
    korean.append((num, k))
    english.append((num, e))
    math.append((num, m))
    science.append((num, s))

korean.sort(key=lambda x: (-x[1], x[0]))
english.sort(key=lambda x: (-x[1], x[0]))
math.sort(key=lambda x: (-x[1], x[0]))
science.sort(key=lambda x: (-x[1], x[0]))
scores = [korean, english, math, science]

reward.append(korean[0][0])

for i in range(1, 4):
    for j in range(4):
        if scores[i][j][0] not in reward:
            reward.append(scores[i][j][0])
            break

print(*reward)