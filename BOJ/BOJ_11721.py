import sys
input = sys.stdin.readline

s = input().rstrip()
c = 0
for _ in range((len(s) // 10) + 1):
    print(s[c: c + 10])
    c += 10