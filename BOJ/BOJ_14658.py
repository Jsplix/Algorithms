import sys
input = sys.stdin.readline
# [BOJ] 14658 하늘에서 별똥별이 빗발친다 / 브루트포스
n, m, l, k = map(int, input().split())
stars = [tuple(map(int, input().split())) for _ in range(k)]
# 별 2개를 기준으로 잡고 트램펄린의 영역을 고려함.
# 기준이 되는 별 2개의 좌-하단의 위치가 트램펄린의 좌-하단 좌표가 됨.
answer = 0
for x1, y1 in stars: # 기준 별 1
    for x2, y2 in stars: # 기준 별 2
        cnt = 0
        for nx, ny in stars:
            if x1 <= nx <= x1 + l and y2 <= ny <= y2 + l:
                cnt += 1
        answer = max(cnt, answer)

print(k - answer)