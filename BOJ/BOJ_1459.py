import sys
input = sys.stdin.readline
# [BOJ] 1459 걷기 / 수학, 많은 조건 분기
x, y, w, s = map(int, input().split())

t1 = (x + y) * w # 가로, 세로만으로 이동

if (x + y) % 2 == 0: t2 = max(x, y)*s # only 대각선
else: t2 = (max(x, y)-1)*s + w # 가로 또는 세로 이동 1번, 나머지 대각선 이동

t3 = min(x, y)*s + abs(x-y)*w # 가로 또는 세로 이동 + 대각선 이동
print(min(t1, t2, t3))