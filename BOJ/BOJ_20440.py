import sys
from collections import defaultdict
input = sys.stdin.readline
# [BOJ] 20440 🎵니가 싫어 싫어 너무 싫어 싫어 오지 마 내게 찝쩍대지마🎵 - 1 / 정렬, 누적 합, 좌표 압축
n = int(input())
inout = defaultdict(int)
for i in range(n):
    enter, out = map(int, input().split())
    inout[enter] += 1
    inout[out] -= 1

# 좌표 압축 이용
cnt, mx = 0, 0
start, finish = 0, 0
flag = False
# 딕셔너리 key들의 value로 현재 방안에 모기가 몇 마리 있는지 확인.
for k in sorted(inout.keys()):
    cnt += inout[k]
    if cnt > mx: # 모기 최대 수 갱신 -> 시작 시간 갱신
        mx = cnt
        start = k
        flag = True
    elif cnt < mx and cnt + abs(inout[k]) == mx and flag: # 최대 마릿수에서 감소할 경우, 나간 시간 갱신
        finish = k
        flag = False

print(mx)
print(start, finish)