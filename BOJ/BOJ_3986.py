import sys
input = sys.stdin.readline
# [BOJ] 3986 좋은 단어 / 자료 구조, 스택
result = 0
for _ in range(int(input())):
    word = list(input().rstrip())
    a_count = word.count('A')
    b_count = len(word) - a_count

    a_stack, b_stack = [], []
    if a_count % 2 and b_count % 2: continue
    elif a_count % 2 and not b_count % 2: continue
    elif not a_count % 2 and b_count % 2: continue
    else:
        if a_count == 0 or b_count == 0: result += 1; continue
        stack = [word[0]]
        for c in word[1:]:
            if not stack: stack.append(c); continue

            if c == stack[-1]:
                stack.pop()
            else:
                stack.append(c)
        
        if not stack: result += 1

print(result) 