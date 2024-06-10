import sys
input = sys.stdin.readline
# [BOJ] 2590 색종이 / 구현, 그리디, 많은 조건 분기
paper = [0] + [int(input()) for _ in range(6)]

result = 0
result += paper[6] if paper[6] else 0 # length = 6

while paper[5]: # length = 5
    area = 36 - 5*5
    paper[5] -= 1
    paper[1] = max(paper[1]-area, 0)
    result += 1

while paper[4]: # length = 4
    area = 36 - 4*4
    area -= min(paper[2], 5) * 4
    paper[4] -= 1
    paper[2] = max(paper[2]-5, 0)
    paper[1] = max(paper[1]-area, 0)
    result += 1

while paper[3]: # length = 3
    area = 36 - 9 * min(paper[3], 4)
    if paper[3] >= 4:
        paper[3] -= 4
        area = 0
    elif paper[3] == 3:
        area -= 4 * min(1, paper[2])
        paper[3] -= 3
        paper[2] = max(paper[2]-1, 0)
    elif paper[3] == 2:
        area -= 4 * min(3, paper[2])
        paper[3] -= 2
        paper[2] = max(paper[2]-3, 0)
    elif paper[3] == 1:
        area -= 4 * min(5, paper[2])
        paper[3] -= 1
        paper[2] = max(paper[2]-5, 0)
    
    paper[1] = max(paper[1]-area, 0)
    result += 1

while paper[2]: # length = 2
    area = 36 - 4 * min(paper[2], 9)
    paper[2] = max(paper[2]-9, 0)
    paper[1] = max(paper[1]-area, 0)
    result += 1

while paper[1]:
    paper[1] = max(paper[1]-36, 0)
    result += 1

print(result)