import sys
input = sys.stdin.readline
# [BOJ] 25640 MBTI / 구현, 문자열
mbti = input().rstrip()
count = 0
for _ in range(int(input())):
    if mbti == input().rstrip():
        count += 1
print(count)