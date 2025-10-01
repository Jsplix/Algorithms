import sys
input = sys.stdin.readline
# [BOJ] 4806 줄 세기 / 구현
count = 0
while True:
    try:
        a = input().rstrip()
        count += 1
    except:
        break
print(count)