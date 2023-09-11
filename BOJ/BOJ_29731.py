import sys
input = sys.stdin.readline
# [BOJ] 2033년 밈 투표 / 구현, 문자열
promise = ['Never gonna give you up', 'Never gonna let you down', 'Never gonna run around and desert you',
           'Never gonna make you cry', 'Never gonna say goodbye', 'Never gonna tell a lie and hurt you',
           'Never gonna stop']

flag = False
for _ in range(int(input())):
    if input().rstrip() not in promise: 
        flag = True

if flag: print("Yes")
else: print("No")