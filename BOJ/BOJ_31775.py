import sys
input = sys.stdin.readline
# [BOJ] 31775 글로벌 포닉스 / 구현, 문자열
check = {'l': 0, 'k': 0, 'p': 0}
for _ in range(3):
    s = input().rstrip()
    if (s[0] == 'l' or s[0] == 'k' or s[0] == 'p') and not check[s[0]]: check[s[0]] += 1
    else: continue

result = check['l'] + check['k'] + check['p']
print("GLOBAL" if result == 3 else "PONIX")