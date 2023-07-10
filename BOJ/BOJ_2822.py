import sys
input = sys.stdin.readline
# [BOJ] 2822 점수 계산 / 정렬
score = []
for i in range(8):
    score.append((int(input()), i+1))
score.sort(reverse=True)

total = 0
pb = []
for j in range(5):
    total += score[j][0]
    pb.append(score[j][1])
pb.sort()

print(total)
print(*pb)