import sys
input = sys.stdin.readline
# [BOJ] 17294 귀여운 수~ε٩(๑> ₃ <)۶з / 수학, 구현
n = list(map(int, input().rstrip()))
flag = False
if len(n) > 2:
    gap = n[0] - n[1]
    for i in range(1, len(n)-1):
        if n[i] - n[i+1] != gap:
            flag = True
            break
if flag: print("흥칫뿡!! <(￣ ﹌ ￣)>")
else: print("◝(⑅•ᴗ•⑅)◜..°♡ 뀌요미!!")