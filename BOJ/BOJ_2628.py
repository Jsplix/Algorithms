import sys
input = sys.stdin.readline
# [BOJ] 2628 종이자르기 / 정렬
w, h = map(int, input().split())
cut_w = [0, w]
cut_h = [0, h]
for _ in range(int(input())):
    k, c = map(int, input().split())
    # 0 - 가로 / 1 - 세로
    if not k:
        cut_h.append(c)
    else:
        cut_w.append(c)
cut_w.sort()
cut_h.sort()
area = []

for i in range(len(cut_w)-1):
    for j in range(len(cut_h)-1):
        a = cut_w[i+1] - cut_w[i]
        b = cut_h[j+1] - cut_h[j]
        area.append(a * b)
print(max(area)) 