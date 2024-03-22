import sys
input = sys.stdin.readline
# [BOJ] 1213 팰린드롬 만들기 / 구현, 문자열, 그리디
name = sorted(list(input().rstrip()))
front, back = '', ''

count = {}
for c in name:
    if c not in count:
        count[c] = 1
    else: count[c] += 1

brk = 0
mid = ''
for k, v in sorted(count.items(), key=lambda x:(x[0], -x[1])):
    if v % 2: 
        brk += 1
        if brk >= 2: 
            print("I'm Sorry Hansoo")
            exit(0)
        mid += k

    for i in range(v - 1 if v % 2 else v):
        if i % 2 == 0: front += k
        else: back += k

print(front + mid + back[::-1])