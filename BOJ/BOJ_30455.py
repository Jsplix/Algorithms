import sys
input = sys.stdin.readline
# [BOJ] 30455 이제는 더 이상 물러날 곳이 없다 / 애드 혹, 게임 이론, 홀짝성
print("Goose") if int(input()) % 2 == 1 else print("Duck")