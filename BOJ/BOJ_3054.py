import sys
input = sys.stdin.readline
# [BOJ] 3054 피터팬 프레임 / 구현
def peterpan(ch):
    return ['.#.', '#.#', '.' + ch + '.', '#.#', '.#.']

def wendy(ch):
    return ['..*..', '.*.*.', '*.' + ch + '.*', '.*.*.', '..*..']

def concat(ans, fr):
    for i in range(5):
        ans[i] += fr[i]
    return ans

answer = ['.', '.', '#', '.', '.']
fix = ['.', '.', '#', '.', '.']

string = input().rstrip()
for i in range(len(string)):
    if i % 3 == 2: concat(answer, wendy(string[i]))
    else: concat(answer, peterpan(string[i]))
                
    if i % 3 == 0:
        concat(answer, fix)

if len(string) % 3 == 2:
    concat(answer, fix)

print(*answer, sep='\n')