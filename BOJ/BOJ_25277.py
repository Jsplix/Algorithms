import sys
input = sys.stdin.readline
# [BOJ] 25277 Culture / 구현, 문자열
n = int(input())
words = list(input().split())

count = 0
for word in words:
    if word == "he" or word == "him" or word == "she" or word == "her":
        count += 1
print(count)