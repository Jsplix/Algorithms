import sys
input = sys.stdin.readline
# [BOJ] 27880 Gahui and Soongsil University station / 수학, 구현, 문자열, 사칙연산
answer = 0
while True:
    try:
        dir, depth = input().split()
        depth = int(depth)

        if dir == "Es":
            answer += 21*depth
        elif dir == "Stair":
            answer += 17*depth
    except:
        break
print(answer)