from itertools import permutations
import sys
input = sys.stdin.readline
# [BOJ] 2503 숫자 야구 / 구현, 브루트 포스
possible = list(permutations(list(str(i) for i in range(1, 10)), 3))
for _ in range(int(input())):
    num, strike, ball = map(int, input().split())
    num = list(str(num))
    remove_cnt = 0

    for i in range(len(possible)):
        s_cnt, b_cnt = 0, 0
        i -= remove_cnt
        for j in range(3):
            if possible[i][j] == num[j]:
                s_cnt += 1
            elif num[j] in possible[i]:
                b_cnt += 1
        
        if s_cnt != strike or b_cnt != ball:
            possible.remove(possible[i])
            remove_cnt += 1

print(len(possible))