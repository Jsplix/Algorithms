import sys
input = sys.stdin.readline
# [BOJ] 32969 학술대회 참가신청 / 구현, 문자열
dh = ["social", "history", "language", "literacy"]
pb = ["bigdata", "public", "society"]

s = input().rstrip()

for word in dh:
    if word in s:
        print("digital humanities")
        exit(0)

for word in pb:
    if word in s:
        print("public bigdata")
        exit(0)
