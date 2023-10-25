import sys
input = sys.stdin.readline
# [BOJ] 3040 백설 공주와 일곱 난쟁이 / 브루트포스
def back(idx, cnt, dwarf: list):
    if cnt == 7 and sum(dwarf) == 100:
        print(*dwarf, sep='\n')
        exit(0)
    if cnt > 7: return
    
    for i in range(idx, 9):
        dwarf.append(height[i])
        back(i+1, cnt+1, dwarf)
        dwarf.pop()
    
height = list(int(input()) for _ in range(9))
back(0, 0, [])